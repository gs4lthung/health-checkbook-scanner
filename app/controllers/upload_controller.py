import os
from flask import current_app, send_file

from app.services.csv_service import update_csv
from app.services.ocr_service import extract_text_from_image


def process_upload(image_file, csv_file):
    image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_file.filename)
    csv_path = os.path.join(current_app.config['UPLOAD_FOLDER'], csv_file.filename)

    image_file.save(image_path)
    csv_file.save(csv_path)

    extracted_data = extract_text_from_image(image_path)

    updated_csv_path = update_csv(csv_path, extracted_data)

    os.remove(image_path)

    return send_file(updated_csv_path, as_attachment=True)
