# import speech_recognition as sr

# # 음성 인식기 초기화
# recognizer = sr.Recognizer()

# # 마이크 선택 (시스템에 연결된 마이크를 선택)
# microphone = sr.Microphone()

# # 무한 루프로 음성 감지 및 자막 생성
# with microphone as source:
#     while True:
#         print("Listening...")
#         audio = recognizer.listen(source)

#         try:
#             # 음성을 텍스트로 변환 (한국어로 인식)
#             recognized_text = recognizer.recognize_google(audio, language="ko-KR")
#             print("You said:", recognized_text)

#         except sr.UnknownValueError:
#             print("Google Speech Recognition could not understand audio.")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")

#         except Exception as e:
#             print(f"An error occurred: {e}")

import speech_recognition as sr
import time

# 음성 인식기 초기화
recognizer = sr.Recognizer()

# 마이크 선택 (시스템에 연결된 마이크를 선택)
microphone = sr.Microphone()

# 초기 시간 설정
start_time = time.time()

while True:
    # 현재 시간
    current_time = time.time()

    # 3초마다 음성 인식 실행
    if current_time - start_time >= 3:
        start_time = current_time
        with microphone as source:
            print("Listening...")
            audio = recognizer.listen(source)

            try:
                # 음성을 텍스트로 변환 (한국어로 인식)
                recognized_text = recognizer.recognize_google(audio, language="en-EN")
                print("You said:", recognized_text)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")