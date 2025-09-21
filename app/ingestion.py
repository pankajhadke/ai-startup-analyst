# app/ingestion.py

import io
from google.cloud import vision
from pdf2image import convert_from_path

def extract_text_from_image_bytes(img_bytes):
    """
    Extracts text from raw image bytes using the Google Cloud Vision API.
    This helper function is called by both extract_text_from_file and extract_text_from_pdf.
    """
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=img_bytes)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    if response.error.message:
        raise Exception(f'Error: {response.error.message}')
    
    return texts[0].description if texts else ""

def extract_text_from_file(file_path):
    """
    Extracts text from a local image file (JPG, PNG, etc.).
    """
    with open(file_path, "rb") as image_file:
        content = image_file.read()
    return extract_text_from_image_bytes(content)

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a local PDF file by converting pages to images.
    """
    extracted_text = ""
    try:
        images = convert_from_path(pdf_path)
        for page_num, image in enumerate(images):
            # Convert PIL image to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_bytes = img_byte_arr.getvalue()
            
            extracted_text += f"\n--- Page {page_num + 1} ---\n"
            # Call the helper function directly with image bytes
            extracted_text += extract_text_from_image_bytes(img_bytes)
            
    except Exception as e:
        raise Exception(f"Error processing PDF file: {e}")
        
    return extracted_text
