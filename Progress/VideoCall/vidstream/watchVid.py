from vidstream import ScreenShareClient
import tkinter as tk
import threading
from PIL import Image, ImageTk
import cv2
import io
from PIL import Image

def start_screen_stream():
    screen_client = ScreenShareClient(text_server_ip.get(1.0, 'end-1c'), 9999)

    def update_image():
        while True:
            try:
                frame = screen_client.get_frame()
                image = Image.open(io.BytesIO(frame))
                img = ImageTk.PhotoImage(image)

                # 화면에 표시된 이미지 업데이트
                label_screen.img = img
                label_screen.config(image=img)
                label_screen.update_idletasks()
            except Exception as e:
                print(e)

    update_thread = threading.Thread(target=update_image)
    update_thread.start()

# GUI
window = tk.Tk()
window.title("화면 공유 뷰어")
window.geometry('800x600')

label_server_ip = tk.Label(window, text="서버 IP:")
label_server_ip.pack()

text_server_ip = tk.Text(window, height=1)
text_server_ip.pack()

btn_start_stream = tk.Button(window, text="화면 공유 시작", width=50, command=start_screen_stream)
btn_start_stream.pack(anchor=tk.CENTER, expand=True)

# 화면 공유를 표시할 라벨
label_screen = tk.Label(window)
label_screen.pack()

window.mainloop()