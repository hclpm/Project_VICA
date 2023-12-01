# import socket
# # my current local ip address
# my_ip_address = socket.gethostbyname(socket.gethostname())
# print(f"my_ip_address: {my_ip_address}")


# # create socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # socket info
# server_address = (my_ip_address, 3333)
# print('Start up on {} port {}'.format(*server_address))
# server_socket.bind(server_address)
# # activate socket
# server_socket.listen()
# print('accept wait')
# # listening..
# client_socket, client_address = server_socket.accept()
# while True:
#     try:
#         # data receive (1024byte)
#         data = client_socket.recv(1024)
#         # decode received data
#         data = data.decode()

#         #######
#         print('Received data:', data)
#         #######
#     except Exception as err:  # 예외 발생 시
#         print('Error:', err)
#     # if data == q // quit
#     if data == "q":
#         break
# client_socket.close()
import socket
import textconnect as tx
import threading

my_ip_address = socket.gethostbyname(socket.gethostname())
port = 4444
serport = 3333
server_thread = threading.Thread(target=tx.text_server, args=[serport])
client_thread = threading.Thread(target=tx.text_client, args=("163.152.224.135", port))

server_thread.start()
client_thread.start()