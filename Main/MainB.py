# tkinter = GUI creating library
# GUI
from my_vidstream import StreamingServer, AudioSender, AudioReceiver, CameraClient, text_client, text_server
import tkinter as tk
import socket
import Functions_1 as my
import threading
from tkinter import *


def thread_subtitle():
    # create thread
    subtitle_thread = threading.Thread(target=my.subtitle)
    # start thread
    subtitle_thread.start()
    # wait thread
    subtitle_thread.join()
    print("Subtitle Closed")


# my current local ip address
my_ip_address = socket.gethostbyname(socket.gethostname())
print(f"my_ip_address: {my_ip_address}")

server = StreamingServer(my_ip_address, 1111)
receiver = AudioReceiver(my_ip_address, 2222)

serport = 4450
port = 4451

# button functions

# create server and start listening

# start sharing screen/camera to server in target ip
# warnings: port numbers must be different from self-server's
# warnings: port numbers must match to the target server's

def start_servers():
    server_thread = threading.Thread(target=server.start_server)
    audioreceiver_thread = threading.Thread(target=receiver.start_server)
    subject = box_subjectInput.get("1.0", tk.END).rstrip("\n")
    generateSubtitle_thread = threading.Thread(target=my.subtitle, args=[subject])    
    textserver_thread = threading.Thread(target=text_server, args=[serport])
    server_thread.start()
    audioreceiver_thread.start()
    textserver_thread.start()
    generateSubtitle_thread.start()

def start_connect():
    camera_client = CameraClient(box_ipInput.get(1.0, 'end-1c'), 9999)
    sendCam_thread = threading.Thread(target=camera_client.start_stream)
    audio_sender = AudioSender(box_ipInput.get(1.0, 'end-1c'), 8888)
    audio_thread = threading.Thread(target=audio_sender.start_stream)

    sendCam_thread.start()
    audio_thread.start()

def stop_videoCall():
    box_content = box_ipInput.get("1.0", tk.END).rstrip("\n")
    text_client(box_content, port)
    while True:
        if my.self_stop_state == "stop" and my.opponent_stop_state == "stop":
            server.stop_server()
            receiver.stop_server()
            break
    

# tkinter = GUI creating library
# GUI
import tkinter as tk
from tkinter import *


VC_GUI = Tk()

VC_GUI.title("VICA Client: B")
VC_GUI.geometry("1000x600")
VC_GUI.configure(bg = "#ffffff")

canvas = Canvas(
    VC_GUI,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/Main_13/images/Bg.png")
background = canvas.create_image(
    553.0, 266.5,
    image=background_img)

# 서버 오픈 btn 코드
btn_open_img = PhotoImage(file = "C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/Main_13/images/serverbtn.png")
btn_open = Button(
    VC_GUI,
    image = btn_open_img,
    borderwidth = 0,
    highlightthickness = 0,
    width= 92,
    height=34,
    command = start_servers,
    relief = "flat")
btn_open.pack(anchor =tk.CENTER, expand=True)
# 서버 오픈 btn 위치값
btn_open.place(
    x = 800, y = 355,
    width = 92,
    height = 34)

# 통화 시작 btn 코드
btn_call_img = PhotoImage(file = "C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/Main_13/images/Callbtn.png")
btn_call = Button(
    VC_GUI,
    image = btn_call_img,
    borderwidth = 0,
    highlightthickness = 0,
    width= 92,
    height=34,
    command = start_connect,
    relief = "flat")
btn_call.pack(anchor =tk.CENTER, expand=True)

# 통화 시작 위치값
btn_call.place(
    x = 800, y = 417,
    width = 92,
    height = 34)


# 서버 닫기 btn 코드
btn_server_stop_img = PhotoImage(file = "C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/Main_13/images/Stop.png")
btn_server_stop = tk.Button(
    VC_GUI,
    image = btn_server_stop_img,
    borderwidth = 0,
    highlightthickness = 0,
    width = 92,
    height = 34,
    command = stop_videoCall,
    relief = "flat")
btn_server_stop.pack(anchor =tk.CENTER, expand=True)

# 서버 닫기 btn 위치값 
btn_server_stop.place(
    x = 800, y = 479,
    width = 92,
    height = 34)


# IP 입력칸 코드
label_ipInput_img = PhotoImage(file = "C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/Main_13/images/inputBox.png")
label_ipInput_bg = canvas.create_image(
    780.0, 165.5,
    image = label_ipInput_img)

box_ipInput = Entry(
    bd = 0,
    bg = "#f4f3f3",
    highlightthickness = 0)
box_ipInput = tk.Text(VC_GUI, width=30, height=1)
box_ipInput.pack()

# IP 입력칸 위치값
box_ipInput.place(
    x = 709.0, y = 147,
    width = 142.0,
    height = 31)

# 주제 입력칸 코드
label_subjectInput_img = PhotoImage(file = "C:/Users/js2-3/Desktop/Github/PrivateFiles/Projects/Communication_Assistant/Main_13/images/inputBox.png")
label_subjectInput_bg = canvas.create_image(
    780.0, 246.5,
    image = label_subjectInput_img)

box_subjectInput = Entry(
    bd = 0,
    bg = "#f4f3f3",
    highlightthickness = 0)
box_subjectInput = tk.Text(VC_GUI, width=30, height=1)
box_subjectInput.pack()

# 주제 입력칸 위치값
box_subjectInput.place(
    x = 709.0, y = 228,
    width = 142.0,
    height = 31)

# 루프 시작
VC_GUI.resizable(False, False)
VC_GUI.mainloop()