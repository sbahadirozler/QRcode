from qreader import QReader
import cv2



def decode_qr_codes(image_path):
    qreader = QReader()
    decoded_info = qreader.detect_and_decode(image_path)

    return decoded_info


image_path = 'qrcode.jpeg'
image = cv2.imread(image_path)


decoded_data = decode_qr_codes(image)

if decoded_data:
    print(f"Image: {image_path} -> Decoded Data: {decoded_data}")
else:
    print(f"Image: {image_path} -> QR code not detected or couldn't be decoded.")
