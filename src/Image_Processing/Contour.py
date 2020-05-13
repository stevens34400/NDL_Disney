import cv2
import numpy as np

#def nothing(x):
    #pass

#Read in frame from previous script
frame = cv2.imread('1frame.jpg')
blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

# *** Conversion from BGR to HSV for mask

#cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
#cv2.createTrackbar('h', 'result',0,179,nothing)
#cv2.createTrackbar('s', 'result',0,255,nothing)
#cv2.createTrackbar('v', 'result',0,255,nothing)


#converting to HSV
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

# get info from track bar and appy to result
h = cv2.getTrackbarPos('h','result')
s = cv2.getTrackbarPos('s','result')
v = cv2.getTrackbarPos('v','result')

# Normal masking algorithm
# For now the lower boundary and upper boundary are hard coded
lower_hsv = np.array([7,100,100])
upper_hsv = np.array([13,255,255])

print(lower_hsv)
#print(upper_hsv)
#print(hsv)

mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

# Create contour
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Draw out contour with green outline on frame
#Primarily used for testing purposes
for contour in contours:
        cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

# Crop out everything except for Moana in a rectangle shape
# Updating the mask created
for c in contours:
    (x,y,w,h)=cv2.boundingRect(c)
    #ellipse = cv2.fitEllipse(c)
    #cv2.ellipse(mask,ellipse,(0,255,0),2)
    cv2.rectangle(mask,(x,y),(x+w,y+h),(255,255,255),-1)

# Represents coordinates of the bounding box (Rectangle for now)
# (x,y) - top left corner
# w - width, h - height
#print ("x: ",x)
#print("y: ",y)
#print('w: ',w)
#print('h: ',h)

#Reverse the max to be able to crop out just the character
mask_reversed = cv2.bitwise_not(mask)

#Final output after crop
result = cv2.bitwise_and(cv2.imread('1frame.jpg'),cv2.imread('1frame.jpg'),mask = mask_reversed)

#frame = cv2.bitwise_and(frame,frame,mask=mask)

crop_img = cv2.bitwise_and(frame,frame,mask=mask)
#crop_img = crop_img[y:y+h,x:x+w]


#cv2.imshow("cropped",crop_img)
cv2.imshow("mask", mask)
cv2.imshow('result',result)
cv2.imshow('contour',frame)
cv2.imshow('initial frame',cv2.imread('1frame.jpg'))


cv2.imwrite("1Result.jpg", result)
cv2.imwrite("1Contour.jpg",frame)
cv2.imwrite("1Mask.jpg",mask)



"""
lower_blue = np.array([5, 100, 20])
upper_blue = np.array([15, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

cv2.imshow("Frame", frame)
cv2.imshow("Mask", mask) """

cv2.waitKey(0)
cv2.destroyAllWindows()