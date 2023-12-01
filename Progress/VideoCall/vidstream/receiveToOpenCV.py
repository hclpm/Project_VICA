from vidstream import ScreenShareClient,StreamingServer,CameraClient
import tkinter as tk
import socket
import threading
import cv2
from PIL import Image, ImageTk

# 내 현재 로컬 IP 주소
my_ip_address = socket.gethostbyname(socket.gethostname())
print(f"my_ip_address: {my_ip_address}")

server = StreamingServer(my_ip_address, 3000)
# CameraClient를 만들어 비디오 프레임을 수신합니다.
client = CameraClient(my_ip_address, 3000)

# 버튼 기능

# 서버 수신 시작
def createAndListenToServer():
    t1 = threading.Thread(target=server.start_server)
    t1.start()

    # 비디오 프레임 수신 시작
    t2 = threading.Thread(target=receive_video)
    t2.start()

# 비디오 프레임을 수신하는 함수
def receive_video():
    client.start_server()

# GUI를 비디오 프레임으로 업데이트하는 함수
def update_video():
    try:
        frame = client.get_frame()
        if frame is not None:
            # 프레임을 RGB 형식으로 변환
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # 이미지를 PIL 형식으로 변환
            image = Image.fromarray(image)
            # PIL 이미지를 Tkinter PhotoImage로 변환
            photo = ImageTk.PhotoImage(image=image)

            # 레이블을 새 이미지로 업데이트
            label_video.config(image=photo)
            label_video.image = photo

        # 다음 업데이트를 10 밀리초 후에 예약
        window.after(10, update_video)
    except:
        pass

# GUI
window = tk.Tk()
window.title("ReceiveVid")
window.geometry('300x400')

label_ipInput = tk.Label(window, text="target IP")
label_ipInput.pack()

box_ipInput = tk.Text(window, height=1)
box_ipInput.pack()

btn_listen = tk.Button(window, text="start receiving", width=50, command=createAndListenToServer)
btn_listen.pack(anchor=tk.CENTER, expand=True)

# 비디오 프레임을 표시할 레이블 생성
label_video = tk.Label(window)
label_video.pack()

# 업데이트 함수 호출
update_video()

window.mainloop()