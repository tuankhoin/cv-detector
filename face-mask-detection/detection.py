from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import imutils
import time
import dlib
import os
import cv2

face_detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
landmark_detect = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


vs = VideoStream(src=0).start()
time.sleep(1.0)

while True:

	
	frame = vs.read()
	frame = imutils.resize(frame, width=600)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_detect.detectMultiScale(gray, scaleFactor=1.1,		minNeighbors=5, minSize=(100, 100),		flags=cv2.CASCADE_SCALE_IMAGE)

	for (x, y, w, h) in faces:

		rect = dlib.rectangle(int(x), int(y), int(x + w),
			int(y + h))

		landmark = landmark_detect(gray, rect)
		landmark = face_utils.shape_to_np(landmark)

		(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
		mouth = landmark[mStart:mEnd]

		boundRect = cv2.boundingRect(mouth)
		cv2.rectangle(frame,
					  (int(boundRect[0]), int(boundRect[1])),
					  (int(boundRect[0] + boundRect[2]),  int(boundRect[1] + boundRect[3])), (0,0,255), 2)

		hsv = cv2.cvtColor(frame[int(boundRect[1]):int(boundRect[1] + boundRect[3]),int(boundRect[0]):int(boundRect[0] + boundRect[2])], cv2.COLOR_RGB2HSV)
		sum_saturation = np.sum(hsv[:, :, 1])
		area = int(boundRect[2])*int(boundRect[3])
		avg_saturation = sum_saturation / area

		if avg_saturation>100:
			cv2.putText(frame, "Please wear face mask!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255),
						2)

	cv2.imshow("Camera", frame)

	key = cv2.waitKey(1) & 0xFF
	if key == 27:
		break


cv2.destroyAllWindows()
vs.stop()