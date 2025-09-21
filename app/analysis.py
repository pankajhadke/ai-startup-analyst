# app/analysis.py

import vertexai
from vertexai.generative_models import GenerativeModel

def summarize_text(text):
    # Initialize Vertex AI with your project ID
    vertexai.init(project="phaai-gen", location="us-central1")
    
    # Use a newer, supported generative model for summarization, such as "gemini-2.0-flash".
    model = GenerativeModel("gemini-2.0-flash")

    # The prompt should be carefully constructed to guide the summary.
    prompt = f"""
    Please provide a professional summary of the following pitch deck text. 
    Focus on the company's core business, market opportunity, competitive advantages, and potential risks.

    Pitch Deck Text:
    {text}
    """
    
    response = model.generate_content(prompt)
    return response.text
