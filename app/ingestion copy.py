# app/ingestion.py

from google.cloud import vision

def extract_text_from_file(file_path):
    """Extracts text from a local image file."""
    client = vision.ImageAnnotatorClient()
    
    with open(file_path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    if response.error.message:
        raise Exception(f'Error: {response.error.message}')
    
    return texts[0].description if texts else ""

# You will need to implement logic for PDF, Word, and OneNote files
# Example for PDF (requires pdf2image and PyMuPDF):
from pdf2image import convert_from_path
import io

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF by converting it to images."""
    extracted_text = ""
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_bytes = img_byte_arr.getvalue()
        extracted_text += extract_text_from_file(img_bytes)
    return extracted_text

