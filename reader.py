import cv2
from pdf2image import convert_from_path
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


def read(path):
    result=[]

    if ".pdf" in path:
        pages=convert_from_path(path,350)
    else:
        try:
            pages=[cv2.imread(path)]
        except:
            raise Warning("Please use an image with valid path!!")
    
    for page in pages:
        text = str(pytesseract.image_to_string(page, config='--psm 6'))
        result.append(text)
    
    return result