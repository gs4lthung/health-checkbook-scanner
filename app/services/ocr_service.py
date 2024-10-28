import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows example


def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img, lang="vie")

    name = extract_name(text)

    return {'Name': name}


def extract_name(text):
    keywords = ["Họ và tên:", "Họ và tên (chữ in hoa):", "Tên:", "Tên bệnh nhân:", "Người dùng:"]

    for keyword in keywords:
        if keyword in text:
            name = text.split(keyword, 1)[1].strip()
            return name.split('\n')[0].split(',')[0].strip()

    return 'Tên không được tìm thấy'
