# 1. TakePic.py
# 2. extract face with faceExtraction.ipynb
# 3. Train CNN model and create own model with createModel_CNN.ipynb
# 4. Use trained CNN model in this python file and recognize face + print information on predicted target

import cv2
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image

# 모델 로드
model = load_model("C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/models/CNNmodel_v2_b8_srs_do.h5")

# 얼굴 인식기 초기화 (OpenCV의 Haarcascades 이용)
face_cascade = cv2.CascadeClassifier('C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/models/haarcascade_frontalface_default.xml')

# 웹캠 열기
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # find face
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # on face:
    for (x, y, w, h) in faces:
        face_roi = frame[y:y + h, x:x + w]
        resized_face = cv2.resize(face_roi, (180, 180))
        img_array = image.img_to_array(resized_face)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # model prediction
        predictions = model.predict(img_array)

        # find class with the highest probability
        predicted_class = np.argmax(predictions)

        # information on each labels
        labels = {0: 'HyunChang', 1: 'KwangMin', 2: 'RaeGun'}
        predicted_label = labels[predicted_class]
        if predicted_class == 0:
            name = "Name: HyunChangLee"
            age = "Age: 23"
            uni = "Uni: KoreaUniv"
            hobby = "Hobby: Football"
        elif predicted_class == 1:
            name = "Name: KwangMinBaek"
            age = "Age: 22"
            uni = "Uni: NULL"
            hobby = "Hobby: Game"
        elif predicted_class == 2:
            name = "Name: RaeGunKim"
            age = "Age: 25"
            uni = "Uni: KoreaUniv"
            hobby = "Hobby: LostArk"
        # print probability(Not necessary)
        print("Predictions:", predictions)

        # show information on imshow window
        cv2.putText(frame, name,    (x+w+5, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(frame, age,     (x+w+5, y+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(frame, uni,     (x+w+5, y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(frame, hobby,   (x+w+5, y+75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # show rectangle around face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # show window
    cv2.imshow('Face Recognition', frame)

    # "q" to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()