import cv2
import time
#from Kmeanstest import DominantColors

x=1
y=23

# Create object cap and read in from media file
cap = cv2.VideoCapture('MoanaMovie.mp4')

# Start movie at a later time, test Kmeans algorithm
cap.set(cv2.CAP_PROP_POS_MSEC,111000*y)

# Create time interval for each frame
time_interval = 3

#Check if capture is opened
if (cap.isOpened()==False):
    print("Error opening media file")

# Will keep on reading file while cap object is opened
while(cap.isOpened()):

    # ***Set timer to only capture frame at specified time interval
    #start_time = time.time()
    #elapsed_time = int(start_time - time.time())

    # Capture each frame of object
    ret, frame = cap.read()
    if ret == True:

        #if (elapsed_time == time_interval):
        cv2.imwrite("1frame.jpg", frame)
        x= x+1
        print("frame", x)

        # Display each frame from cap object
        cv2.imshow('Frame',frame)

        #print("2")

        # Create Dominant Colors class from each frame
        #frame = 'frame.jpg'
        #dc = DominantColors(frame, 5)
        #colors = dc.dominantColors()
        #print(colors)


        # Press 'Q' on keyboard to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # If not captured then break out of loop
    else:
        break

cap.release()

cv2.destroyAllWindows()

