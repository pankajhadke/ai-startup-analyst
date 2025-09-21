# web.py

import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# Import functions from your existing app/ modules
from app.ingestion import extract_text_from_file, extract_text_from_pdf
from app.analysis import summarize_text
from app.benchmarking import get_benchmark
from app.risk_assessment import detect_risks
from app.deal_note_generation import save_deal_note

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_startup():
    """Handle the analysis request from the web form and render the results."""
    # ... (Your existing file handling and data extraction logic) ...
    # Use secure_filename to prevent malicious file names
    file = request.files['pitch_deck']
    filename = secure_filename(file.filename)
    file_extension = filename.split('.')[-1].lower()
    temp_file_path = os.path.join("data", filename)
    os.makedirs("data", exist_ok=True)
    file.save(temp_file_path)

    if file_extension == 'pdf':
        text = extract_text_from_pdf(temp_file_path)
    elif file_extension in ['jpg', 'jpeg']:
        text = extract_text_from_file(temp_file_path)
    else:
        # Instead of returning JSON, render an error page
        return render_template('error.html', error_message="Unsupported file format."), 400

    # ... (Your existing analysis logic) ...
    sector = request.form.get('sector', 'B2B SaaS')
    geo = request.form.get('geo', 'US')
    startup_metrics = {
        "churn_rate": float(request.form.get('churn_rate', 0.18)),
        "market_size": float(request.form.get('market_size', 5e9)),
    }
    
    summary = summarize_text(text)
    benchmark = get_benchmark(sector, geo)
    
    if not benchmark:
        risks = ["No benchmark data found for the specified sector and geography."]
        benchmark = {"avg_churn_rate": "N/A", "avg_market_size": "N/A"}
    else:
        risks = detect_risks(startup_metrics, benchmark)

    deal_note = {
        "summary": summary,
        "benchmark": benchmark,
        "risks": risks,
    }

    save_deal_note("web_user_123", deal_note)

    # --- Render a new HTML template with the deal note data ---
    return render_template('results.html', deal_note=deal_note)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True)
