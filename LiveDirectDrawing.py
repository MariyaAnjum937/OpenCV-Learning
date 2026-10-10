import cv2
import numpy as np

def draw(event, x, y, flags, params):
    if event == 1:
        cv2.circle(img, center=(x,y), radius=20, color=(0,255,0), thickness=-1)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", draw)

img = np.zeros((512, 512, 3))

while True:
    cv2.imshow("window", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()