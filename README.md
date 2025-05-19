⸻


# 🧠 Mediapipe 기반 실시간 제스처 및 사운드 인식 프로젝트

이 프로젝트는 **Mediapipe**, **OpenCV**, **음성 처리**, 그리고 **딥러닝 모델 활용**을 통해 다양한 **실시간 얼굴/제스처/소리 인식** 기능을 구현한 예제입니다. 웹캠과 마이크를 활용하여 사용자의 행동을 감지하고, 오디오 피드백을 제공합니다.

---

## 📦 주요 기능

| 기능 | 설명 |
|------|------|
| 👋 V 제스처 인식 | 손가락으로 V자를 만들면 인식하고 카운트 |
| 🙌 박수 인식 | 박수 소리를 인식하고 오디오 피드백 |
| 💬 음성 인식 | 특정 음성을 인식하여 효과음 재생 |
| 🧍‍♂️ 던지기 제스처 인식 | 던지는 듯한 손 제스처 인식 |
| 😊 얼굴 인식 | 사용자의 얼굴을 등록하고 인식 가능 |

---

## 🗂️ 프로젝트 구조

.
├── Face_detection.py         # Mediapipe 기반 얼굴 인식   
├── Clap_detection.py         # 박수 소리 인식 및 반응   
├── count_V_detection.py      # 손가락 V 제스처 인식   
├── Throwing_detection.py     # 던지기 제스처 인식   
├── sound_detection.py        # 사운드(음성) 인식 및 효과음 재생   
├── registered_face.npy       # 등록된 얼굴 데이터   
├── kick.mp3                  # 킥 드럼 효과음   
├── hi_hat.mp3                # 하이햇 효과음   
├── wow.mp3                   # “Wow” 효과음   
└── README.md                 # 설명 파일   

---

## ⚙️ 설치 방법

### 1. 가상환경(선택)
```bash
python -m venv venv
source venv/bin/activate  # Windows는 .\venv\Scripts\activate

2. 라이브러리 설치

pip install mediapipe opencv-python numpy pygame sounddevice

※ 필요 시 soundfile, scipy 등의 라이브러리도 추가로 설치해 주세요.

⸻

🚀 실행 방법

얼굴 인식

python Face_detection.py

박수 소리 인식

python Clap_detection.py

손가락 V 제스처 인식

python count_V_detection.py

던지기 제스처 인식

python Throwing_detection.py

음성 및 효과음 인식

python sound_detection.py


⸻

🎵 효과음

파일	설명
kick.mp3	박수나 제스처에 반응하는 킥 드럼 소리
hi_hat.mp3	박수 후 재생되는 하이햇 사운드
wow.mp3	감탄을 표현하는 음성 효과


⸻

🧠 기술 스택
	•	Python 3.8+
	•	Mediapipe
	•	OpenCV
	•	NumPy
	•	Pygame
	•	SoundDevice

⸻

📝 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자유롭게 사용 및 수정하실 수 있습니다.

⸻

📌 참고
	•	이 프로젝트는 로컬 카메라 및 마이크 접근 권한이 필요합니다.
	•	모든 테스트는 macOS M3 환경에서 수행되었습니다.

---
