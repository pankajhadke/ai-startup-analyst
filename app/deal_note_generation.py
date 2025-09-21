# app/deal_note_generation.py

import json
import os

def save_deal_note(startup_id, deal_note):
    """Saves the deal note to a local JSON file."""
    output_dir = "./deal_notes"
    os.makedirs(output_dir, exist_ok=True)
    
    file_path = os.path.join(output_dir, f"{startup_id}.json")
    with open(file_path, "w") as f:
        json.dump(deal_note, f, indent=4)
    print(f"Deal note saved to {file_path}")
