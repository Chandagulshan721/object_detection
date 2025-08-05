"""import imutils
import cv2


redLower = (38,10,10)
redUpper = (136, 215, 80)

camera = cv2.VideoCapture(0)


while True:
    (grabbed, frame) = camera.read()

    frame = imutils.resize(frame, width=1000)

    blurred = cv2.GaussianBlur(frame, (11,11), 0)

    hsv = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv, redLower, redUpper)
    mask=cv2.erode(mask, None, iterations=2)
    mask=cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    center = None
    if len(cnts) > 0:
        c = max(cnts, key= cv2.contourArea)
        ((x,y),radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)) , int(radius), (0,255,255),2)
            cv2.circle(frame, center, 5, (0,0,255), -1)
            print(center,radius)
            if radius > 250:
                print("stop")
            else:
                if(center[0]<150):
                    print("right")
                elif(center[0]>450):
                    print("left")
                else:
                    print("stop")
    
    cv2.imshow("FRAME",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()"""


"""
import imutils
import cv2

# Set HSV range for object color (tuned using your calibration)
redLower = (38, 10, 10)
redUpper = (136, 215, 80)

camera = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = camera.read()
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
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            if radius > 10:
                # Draw object outline
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                
                print(center, radius)

                if radius > 250:
                    print("stop")
                else:
                    if center[0] < 300:
                        print("right")
                    elif center[0] > 700:
                        print("left")
                    else:
                        print("stop")
        else:
            print("No valid center found")

    else:
        print("No object detected")

    cv2.imshow("FRAME", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()"""


import cv2
import imutils

# HSV range of the object (adjust as needed)
redLower = (38, 10, 10)
redUpper = (136, 215, 80)

# Start camera
camera = cv2.VideoCapture(0)

while True:
    grabbed, frame = camera.read()
    frame = imutils.resize(frame, width=1000)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, redLower, redUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    direction = "No object"

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)

        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        else:
            center = (int(x), int(y))  # fallback

        if radius > 10:
            # Draw object circle and center
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

            # Decide direction based on x-position
            if radius > 250:
                direction = "Stop"
            elif center[0] < 300:
                direction = "Right"
            elif center[0] > 700:
                direction = "Left"
            else:
                direction = "Stop"

    # Display direction on screen
    cv2.putText(frame, f"Direction: {direction}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 3)

    cv2.imshow("FRAME", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

