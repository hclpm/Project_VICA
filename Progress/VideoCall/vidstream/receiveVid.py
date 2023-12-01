from vidstream import ScreenShareClient, VideoClient, StreamingServer
import tkinter as tk
import socket
import threading



# my current local ip address
my_ip_address = socket.gethostbyname(socket.gethostname())
print(f"my_ip_address: {my_ip_address}")

server = StreamingServer(my_ip_address, 3000)

# button functions

# start listening to the server
def createAndListenToServer():
    t1 = threading.Thread(target=server.start_server)
    t1.start()



# tkinter = GUI creating library
# GUI
window = tk.Tk()
window.title("ReceiveVid")
window.geometry('300x200')

label_ipInput = tk.Label(window, text="target ip")
label_ipInput.pack()

box_ipInput = tk.Text(window, height=1)
box_ipInput.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=createAndListenToServer)
btn_listen.pack(anchor=tk.CENTER, expand=True)


window.mainloop()