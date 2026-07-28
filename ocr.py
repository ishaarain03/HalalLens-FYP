import re
import easyocr

_ocr = easyocr.Reader(['en'])
_stops = r',|;|:|\.|\(|\)|\n'

def extract_ingredients(image_path: str) -> str:
    result = _ocr.readtext(image_path)
    text = ' '.join([x[1] for x in result])
    text = text.lower().strip()

    parts = text.split('ingredients')
    text = parts[1] if len(parts) > 1 else text

    ings = re.split(_stops, text)
    ings = [
        re.sub(_stops, '', ing).strip().lower()
        for ing in ings
        if ing
    ]
    ings = [
        ing
        for ing in ings if
        ing and len(ing) > 1
    ]
    return ings
