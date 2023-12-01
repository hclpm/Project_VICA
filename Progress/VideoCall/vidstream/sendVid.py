from vidstream import ScreenShareClient, VideoClient, StreamingServer,  CameraClient
import tkinter as tk
import socket
import threading

# my current local ip address
my_ip_address = socket.gethostbyname(socket.gethostname())
print(f"my_ip_address: {my_ip_address}")


# button functions
def start_screen_sharing():
    screen_client = ScreenShareClient(box_ipInput.get(1.0, 'end-1c'), 3000)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()
def start_camera_stream():
    camera_client = CameraClient(box_ipInput.get(1.0, 'end-1c'), 3000)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()


# tkinter = GUI creating library
# GUI
window = tk.Tk()
window.title("SendVid")
window.geometry('300x200')

label_ipInput = tk.Label(window, text="target ip")
label_ipInput.pack()

box_ipInput = tk.Text(window, height=1)
box_ipInput.pack()

btn_streamScreen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_streamScreen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor =tk.CENTER, expand=True)

window.mainloop()