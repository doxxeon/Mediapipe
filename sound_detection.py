
import cv2
import mediapipe as mp
import pygame

# Initialize sound
pygame.mixer.init()
sounds = {
    "kick": pygame.mixer.Sound("/Users/kimdohyeon/Desktop/Mediapipe/kick.mp3"),
    "hi_hat": pygame.mixer.Sound("/Users/kimdohyeon/Desktop/Mediapipe/hi_hat.mp3"),
    "wow": pygame.mixer.Sound("/Users/kimdohyeon/Desktop/Mediapipe/wow.mp3")
}

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # 손가락 위치
                landmarks = hand_landmarks.landmark
                tip_ids = [4, 8, 12, 16, 20]

                fingers = []

                # 엄지: x축 비교
                if landmarks[4].x < landmarks[3].x:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # 나머지 손가락: y축 비교
                for tip_id in tip_ids[1:]:
                    if landmarks[tip_id].y < landmarks[tip_id - 2].y:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total_fingers = sum(fingers)

                # 주먹: 모두 접힘
                if total_fingers == 0:
                    cv2.putText(image, "🥁 Kick", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    sounds["kick"].play()

                # 손 다 폈을 때
                elif total_fingers == 5:
                    cv2.putText(image, "✨ Hi-hat", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    sounds["hi_hat"].play()

                # 손가락 총 모양: 엄지, 검지만 펴짐
                elif fingers == [1, 1, 0, 0, 0]:
                    cv2.putText(image, "🎉 WOW!", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                    sounds["wow"].play()

        cv2.imshow('DJ Mode', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()