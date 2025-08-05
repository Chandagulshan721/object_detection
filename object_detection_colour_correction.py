import cv2
import numpy as np

def nothing(x):
    pass

# Create a window for trackbars
cv2.namedWindow("HSV Calibration")

# Create trackbars for HSV values
cv2.createTrackbar("Lower-H", "HSV Calibration", 0, 179, nothing)
cv2.createTrackbar("Lower-S", "HSV Calibration", 0, 255, nothing)
cv2.createTrackbar("Lower-V", "HSV Calibration", 0, 255, nothing)
cv2.createTrackbar("Upper-H", "HSV Calibration", 179, 179, nothing)
cv2.createTrackbar("Upper-S", "HSV Calibration", 255, 255, nothing)
cv2.createTrackbar("Upper-V", "HSV Calibration", 255, 255, nothing)

# Open the webcam
camera = cv2.VideoCapture(0)

while True:
    # Read frame
    grabbed, frame = camera.read()
    if not grabbed:
        break

    # Convert frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get current trackbar positions
    lower_h = cv2.getTrackbarPos("Lower-H", "HSV Calibration")
    lower_s = cv2.getTrackbarPos("Lower-S", "HSV Calibration")
    lower_v = cv2.getTrackbarPos("Lower-V", "HSV Calibration")
    upper_h = cv2.getTrackbarPos("Upper-H", "HSV Calibration")
    upper_s = cv2.getTrackbarPos("Upper-S", "HSV Calibration")
    upper_v = cv2.getTrackbarPos("Upper-V", "HSV Calibration")

    # Define lower and upper bounds
    lower_bound = (lower_h, lower_s, lower_v)
    upper_bound = (upper_h, upper_s, upper_v)

    # Create a mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Show the original frame and mask
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()













































"""import imutils  # Resize
import cv2

redLower = (95, 49, 100)
redUpper = (154, 255, 255)

camera = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break  # Stop if frame not grabbed

    frame = imutils.resize(frame, width=1000)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, redLower, redUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)

        if M["m00"] != 0:  # Prevent division by zero
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

                print(center, radius)
                if radius > 250:
                    print("Stop")
                else:
                    if center[0] < 150:
                        print("Right")
                    elif center[0] > 450:
                        print("Left")
                    elif radius < 250:
                        print("Front")
                    else:
                        print("Stop")

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)  # Corrected waitKey spelling
    if key == ord("q"):  # Added missing colon
        break

camera.release()
cv2.destroyAllWindows()"""














































"""import imutils #Resize
import cv2

redLower = (95, 49, 100)
redUpper = (154, 255, 255)


camera=cv2.VidoeCapture(1)

while True:
    (grabbed, frame) = camera.read()
    frame = imutils.resize(frame,width=1000)
    blurred = cv2.GaussianBlur(frame, (11,11),0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, redlower, redUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) >0 :
        c = max(cnts, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]) , int(M["m01"] / M["m00"])

         if radius > 10:
            cv2.circle(frame,(int(x), int(y)),int(y)), int(radius),(0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255), -1)
                  print(center, radius)
            if radius >250:
                  print("stop")
            else:
                   if(center[0]<150):
                       print("Right")
                   elif(center[0]>450):
                       print("left")
                   elif(radius<250):
                       print("Front")
                   else:
                       print("stop")
    cv2.imshow("frame",frame)
    key = cv2.waitkey(1)
    if key == ord("q")
         break


camera.release()
cv2.destroyAllWindows()"""




