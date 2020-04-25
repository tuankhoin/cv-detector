import cv2 
import keras
import numpy as np

mask_model = keras.models.load_model('/face_mask_data.h5')
video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/haarcascade_frontalface_default.xml')

while(True):
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))

    print("Found {0} face(s)!".format(len(faces)))

    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (36,255,12), 1)
        current_image = np.array(frame)

        model_prediction = mask_model.predict(current_image.reshape(-1, 160, 160, 3)) == mask_model.predict(current_image.reshape(-1,160,160,3)).max()
        result = np.sum(mask_model.predict(current_image.reshape(-1,160,160,3)), axis = 0)

        if result[0] >= result[1]:
            display_string = 'With Mask'
        else:
            display_string = 'Without Mask'

        cv2.putText(frame, display_string, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36, 255, 12), 1)
   
video.release()
cv2.destroyAllWindows()