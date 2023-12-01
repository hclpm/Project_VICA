import sys
import requests
import keys as my
client_id = my.CLOVA_ClientID()
client_secret = my.CLOVA_ClientSecret()
lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}


###################################################

import speech_recognition as sr

# 음성 인식기 초기화
recognizer = sr.Recognizer()

# 마이크 선택 (시스템에 연결된 마이크를 선택)
microphone = sr.Microphone()

# 무한 루프로 음성 감지 및 자막 생성
with microphone as source:
    while True:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            data = audio
            response = requests.post(url,  data=data, headers=headers)
            rescode = response.status_code
            if(rescode == 200):
                print (response.text)
            else:
                print("Error : " + response.text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

        except Exception as e:
            print(f"An error occurred: {e}")