

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


#################################################


def speech_translator():
    import speech_recognition as sr

    # 음성 인식기 초기화
    recognizer = sr.Recognizer()
    # 마이크 선택 (시스템에 연결된 마이크를 선택)
    microphone = sr.Microphone()

    # 무한 루프로 음성 감지 및 자막 생성
    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            # 음성을 텍스트로 변환 (한국어로 인식)
            recognized_text = recognizer.recognize_google(audio, language="ko-KR")
            translated_text = translation(recognized_text)
            print("You said:   ", recognized_text)
            print("In English: ", translated_text)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    return recognized_text, translated_text

while True:
    speech_translator()
    print("hello")