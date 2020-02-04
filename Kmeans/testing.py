import cv2
import numpy as np

low = np.uint8([223,126,92])
hsvlow = cv2.cvtColor(low , cv2.COLOR_BGR2HSV)
print(hsvlow)