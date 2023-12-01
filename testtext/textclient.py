# import threading


# ip_address = "163.152.224.134"
# port = 3333

# def text_client(ip_address, port):
#     import socket

#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     data = ""
#     server_address = (ip_address, port)

#     # connect to socket
#     print(type(server_address))
#     client_socket.connect(server_address)

#     while data != 'quit':
#         try:
#             # input value
#             data = input("")
#             data = data.encode()
#             client_socket.send(data)
#             # if data == 'quit' // quit
#             if data == b'q':
#                 client_socket.close()
#                 break
#         except Exception as e:
#             print('Error:', e)

# textClient_thread = threading.Thread(target=text_client, args=(ip_address, port))
# textClient_thread.start()
import socket
import textconnect as tx
import threading
my_ip_address = socket.gethostbyname(socket.gethostname())
port = 3333
serport = 4444
client_thread = threading.Thread(target=tx.text_client, args=("163.152.224.134", port))
server_thread = threading.Thread(target=tx.text_server, args=[serport])

server_thread.start()
client_thread.start()
