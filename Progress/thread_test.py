import threading
import time

def cam_thread():
    # Placeholder for actual cam_thread functionality
    print("cam_thread started")
    time.sleep(3)  # Simulating some work
    print("cam_thread finished")

def speech_translator():
    # Placeholder for actual speech_translator functionality
    print("speech_translator started")
    time.sleep(5)  # Simulating some work
    print("speech_translator finished")

if __name__ == "__main__":
    # 쓰레드 생성
    cam_thread = threading.Thread(target=cam_thread)
    speech_translator_thread = threading.Thread(target=speech_translator)

    # 쓰레드 시작
    cam_thread.start()
    speech_translator_thread.start()

    # 메인 쓰레드에서 쓰레드가 종료될 때까지 대기
    cam_thread.join()
    speech_translator_thread.join()

    print("All threads have finished, exiting main thread")