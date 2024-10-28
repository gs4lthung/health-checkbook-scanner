from flask import Blueprint, render_template, request

from app.controllers.upload_controller import process_upload

main_routes = Blueprint('main', __name__)


@main_routes.route('/')
def index():
    return render_template('index.html')


@main_routes.route('/upload', methods=['POST'])
def upload_file():
    image_file = request.files.get('image')
    csv_file = request.files.get('csv')
    if not image_file or not csv_file:
        return 'Hãy đăng lên đầy đủ ảnh và file.', 400
    return process_upload(image_file, csv_file)
