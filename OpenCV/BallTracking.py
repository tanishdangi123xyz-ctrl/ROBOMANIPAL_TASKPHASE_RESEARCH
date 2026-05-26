import cv2 as cv
import numpy as np

videoCapture = cv.VideoCapture("vc1.mov")
prevCircle = None

dist = lambda x1,y1,x2,y2: (x1-x2)**2 + (y1-y2)**2

frame_width = int(videoCapture.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(videoCapture.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(videoCapture.get(cv.CAP_PROP_FPS))

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('tracked_output.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = videoCapture.read()
    if not ret: break

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(grayFrame, (17, 17), 0)

    circles = cv.HoughCircles(blurred, cv.HOUGH_GRADIENT, 1.4, 100, param1=100, param2=20, minRadius=30, maxRadius=80)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None:
                chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i

        cv.circle(frame, (int(chosen[0]), int(chosen[1])), int(chosen[2]), (0, 0, 400), 4)

    out.write(frame)
    cv.imshow("circles", frame)
    if cv.waitKey(1) & 0xFF == ord('q'): break

videoCapture.release()
out.release()
cv.destroyAllWindows()