import cv2
import winsound

cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    frame1 = cv2.flip(frame1, 3)
    ret2, frame2 = cam.read()
    frame2 = cv2.flip(frame2, 3)
    difference = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, (5, 5), iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.Beep(200, 200)

    if cv2.waitKey(10) == ord('q'):
        break

    cv2.imshow("Utsho Security Cam", frame1)
