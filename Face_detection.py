import cv2
import streamlit as st
import numpy as np
import mediapipe as mp
import face_recognition  # face_recognition 라이브러리 활용
from PIL import Image

st.title('🙋🏻‍♂️ Face Recognizer')

# 얼굴 임베딩을 위한 함수
def get_face_embedding(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    return encodings[0] if encodings else None

# 등록된 얼굴 불러오기 (예: 저장된 임베딩)
try:
    registered_face = np.load('/Users/kimdohyeon/Desktop/Mediapipe/registered_face.npy')
except FileNotFoundError:
    registered_face = None

# Streamlit 카메라 입력 받기
img_file = st.camera_input("얼굴을 찍어주세요 📸")

if img_file:
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)

    embedding = get_face_embedding(frame)

    if embedding is not None:
        if registered_face is not None:
            # Cosine 유사도 계산
            similarity = np.dot(embedding, registered_face) / (np.linalg.norm(embedding) * np.linalg.norm(registered_face))
            st.write(f"유사도: {similarity:.2f}")
            st.success("본인입니다!") if similarity > 0.6 else st.error("다른 사람입니다!")
        else:
            if st.button("이 얼굴을 등록하기"):
                np.save('registered_face.npy', embedding)
                st.success("얼굴이 등록되었습니다!")
    else:
        st.warning("얼굴이 감지되지 않았어요 😢")