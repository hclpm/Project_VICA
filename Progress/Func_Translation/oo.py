

def translation(message):
    import urllib.request
    import keys as my
    import json
    client_id = my.PAPAGO_ClientID()
    client_secret = my.PAPAGO_ClientSecret()
    encText = urllib.parse.quote(message)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_data = json.loads(response_body.decode('utf-8'))
        translated_text = response_data['message']['result']['translatedText']
        return translated_text
    else:
        print("Error Code:" + rescode)


#################################################################
import pynput.keyboard
import speech_recognition as sr
import threading
import time

# 음성 인식기 초기화
recognizer = sr.Recognizer()

# 마이크 선택 (시스템에 연결된 마이크를 선택)
microphone = sr.Microphone()

# 음성 입력을 저장할 변수
recognized_text = ""

# 키보드 이벤트 핸들러
def on_key_release(key):
    global recognized_text

    if key == pynput.keyboard.Key.esc:
        # "esc" 키를 누르면 프로그램 종료
        return False
    if key.char == 't':
        # "t" 키를 누르면 음성 인식 시작
        with microphone as source:
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            # 음성을 텍스트로 변환 (한국어로 인식)
            recognized_text = recognizer.recognize_google(audio, language="ko-KR")
            print("You said:", recognized_text)
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

# 키보드 리스너 시작
keyboard_listener = pynput.keyboard.Listener(on_release=on_key_release)
keyboard_listener.start()

# 무한 루프로 번역 실행
while True:
    if recognized_text:
        translation_result = translation(recognized_text)
        print("In English:", translation_result)
        recognized_text = ""  # 음성 인식 결과 초기화
    time.sleep(1)  # 1초 간격으로 확인