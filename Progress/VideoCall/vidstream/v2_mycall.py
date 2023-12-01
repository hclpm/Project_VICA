from vidstream import ScreenShareClient, VideoClient, StreamingServer
import tkinter as tk
import socket
import threading
import requests

# my current local ip address
local_ip_address = socket.gethostbyname(socket.gethostname())
print(f"local_ip_address: {local_ip_address}")

server = StreamingServer(local_ip_address, 8888)

# button functions

# start listening to the server
def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t1.start()

# start receiving screen-sharing data from the server
def start_screen_sharing():
    screen_client = ScreenShareClient(box_ipInput.get(1.0, 'end-1c'), 9999)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()



# tkinter = GUI creating library
# GUI
window = tk.Tk()
window.title("window name")
window.geometry('300x200')

label_ipInput = tk.Label(window, text="target ip")
label_ipInput.pack()

box_ipInput = tk.Text(window, height=1)
box_ipInput.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_streamScreen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_streamScreen.pack(anchor=tk.CENTER, expand=True)


window.mainloop()