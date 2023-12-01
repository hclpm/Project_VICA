from google.cloud import speech_v1p1beta1 as speech
import pyaudio

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/js2-3/Desktop/Github/Desktop_sync/Projects/VoiceRecognition/request.json"

# Google Cloud Speech-to-Text API 설정
client = speech.SpeechClient()
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,  # 적절한 샘플 속도로 설정
    language_code="ko-KR",
    enable_automatic_punctuation=True,
    model="default",
)

# 오디오 스트리밍 설정
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=1024)

# 실시간 음성 인식 및 자막 출력
print("실시간 음성 인식 시작...")

stream.start_stream()
while True:
    try:
        audio_data = stream.read(1024)  # 오디오 데이터를 읽음
        audio = speech.RecognitionAudio(content=audio_data)
        response = client.streaming_recognize(config=config, audio=audio)  # Google Cloud API를 사용하여 음성을 텍스트로 변환
        
        for result in response:
            for alternative in result.alternatives:
                print("자막: {}".format(alternative.transcript))  # 변환된 텍스트를 출력
    
    except KeyboardInterrupt:
        print("실시간 음성 인식 종료.")
        stream.stop_stream()
        stream.close()
        p.terminate()
        break