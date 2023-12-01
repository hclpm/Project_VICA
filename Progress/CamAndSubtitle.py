# list of necessary libraries:
# PIL, numpy, threading, cv2, dlib 
# --> can be installed via pip install~

import Functions_1 as my
import threading

def main():
    # create thread
    cam_thread = threading.Thread(target=my.camera)
    subtitle_thread = threading.Thread(target=my.subtitle)

    # start thread
    cam_thread.start()
    subtitle_thread.start()

    # wait thread
    subtitle_thread.join()
    cam_thread.join()
    print("All Thread Closed")

# activate main()
if __name__ == "__main__":
    main()
    print("System down")



# audio_format=pyaudio.paInt16, channels=1, rate=44100, frame_chunk=4096
