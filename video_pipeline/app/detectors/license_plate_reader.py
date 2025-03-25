import easyocr

reader = easyocr.Reader(['en'])

def read_plate(frame):
    results = reader.readtext(frame)
    plates = [r[1] for r in results if len(r[1]) >= 5 and any(c.isdigit() for c in r[1])]
    return plates
