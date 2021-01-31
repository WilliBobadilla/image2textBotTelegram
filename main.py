try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import os
import errno

def mkdir():
    try:
        os.mkdir('images')
        os.mkdir('text')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convertidor(path_name):
    text = pytesseract.image_to_string(Image.open(path_name))
    print(text)
    return text

def lengh(path_name):
    text = pytesseract.image_to_string(Image.open(path_name))
    leng = len(text)
    print(leng)
    return leng