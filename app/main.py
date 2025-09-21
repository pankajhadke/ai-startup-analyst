from ingestion import extract_text_from_file
from analysis import summarize_text
from benchmarking import get_benchmark
from risk_assessment import detect_risks
from deal_note_generation import save_deal_note

def main():
    startup = {
        "pitch_deck": "./data/sample_pitch_deck.jpg",
        "sector": "B2B SaaS",
        "geo": "US",
        "id": "startup123",
        "metrics": {"churn_rate": 0.18, "market_size": 5e9},
    }

    text = extract_text_from_file(startup["pitch_deck"])
    summary = summarize_text(text)
    benchmark = get_benchmark(startup["sector"], startup["geo"])
    
    # Pass both arguments to detect_risks to fix the TypeError
    risks = detect_risks(startup["metrics"], benchmark)

    deal_note = {
        "summary": summary,
        "benchmark": benchmark,
        "risks": risks,
    }

    save_deal_note(startup["id"], deal_note)
    print("Deal note created successfully.")

if __name__ == "__main__":
    main()
