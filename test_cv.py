# import numpy as np
# import cv2
# import time
#
#
# t = time.time()
# while time.time() -t < 2:
#     cap = cv2.VideoCapture(0)
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# # cv2.imshow('frame',gray)
# # cv2.imwrite('ishan.png',gray)
# gray  = cv2.resize(gray,None,fx=28/1280, fy=28/720, interpolation = cv2.INTER_CUBIC)
# cv2.imwrite('ishan.png',gray)
#
# # print(gray.shape)
# # time.sleep(5)
# cap.release()


# When everything done, release the capture
import numpy as np
import cv2
from PIL import Image

from resizeimage import resizeimage

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray,150,180)
    fgmask = fgbg.apply(edged)

    cv2.imshow('frame',fgmask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
