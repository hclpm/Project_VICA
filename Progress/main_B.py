from my_vidstream import ScreenShareClient, StreamingServer, CameraClient
import tkinter as tk
import socket
import Functions_1 as my
import threading


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

server = StreamingServer(my_ip_address, 2222)

# button functions

# start sharing screen/camera to server in target ip
# warnings: port numbers must be different from self-server's
# warnings: port numbers must match to the target server's
def start_camera_stream():
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()
    camera_client = CameraClient(box_ipInput.get(1.0, 'end-1c'), 1111)
    sendCam_thread = threading.Thread(target=camera_client.start_stream)
    generateSubtitle_thread = threading.Thread(target=my.subtitle)
    sendCam_thread.start()
    generateSubtitle_thread.start()


# tkinter = GUI creating library
# GUI
VC_GUI = tk.Tk()
VC_GUI.title("VideoCall GUI_self")
VC_GUI.geometry('300x200')

# server button
# btn_listen = tk.Button(VC_GUI, text="Start Listening", width=50, command=createAndListenToServer)
# btn_listen.pack(anchor=tk.CENTER, expand=True)

# ip input box
label_ipInput = tk.Label(VC_GUI, text="target ip")
label_ipInput.pack()
box_ipInput = tk.Text(VC_GUI, height=1)
box_ipInput.pack()

# # sharing buttons
# btn_streamScreen = tk.Button(VC_GUI, text="Start Screen Sharing", width=50, command=start_screen_sharing)
# btn_streamScreen.pack(anchor=tk.CENTER, expand=True)
btn_camera = tk.Button(VC_GUI, text="Start Video Call", width=50, command=start_camera_stream)
btn_camera.pack(anchor =tk.CENTER, expand=True)

# exit button
btn_finishCall = tk.Button(VC_GUI, text="Stop Video Call", width=50)
btn_finishCall.pack(anchor =tk.CENTER, expand=True)


VC_GUI.mainloop()