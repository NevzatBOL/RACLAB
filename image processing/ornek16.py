#-*-coding: cp1254-*-
###QR Kod Okuma###

import cv2
import zbar
from PIL import Image

cam = cv2.VideoCapture(0)

scanner = zbar.ImageScanner()
scanner.parse_config('enable')

last_symbol =  None

while True:
    ret, frame = cam.read()
    if not ret:
	  continue
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY, dstCn=0)
    pil = Image.fromarray(gray)
    width, height = pil.size
    raw = pil.tobytes()
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)

    for symbol in image:
	if symbol.data!=last_symbol:
		print '"%s"' % symbol.data
		last_symbol=symbol.data

    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == 27:
    	break

cam.release()
cv2.destroyAllWindows()
