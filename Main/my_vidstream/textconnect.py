from Functions_1 import giveKortext, client_conversation_append
import Functions_1 as my
import pickle
data = ""
prev_data = ""

# append received text data to my dialogue
def text_server(port):
    global data, prev_data
    import socket
    # my current local ip address
    my_ip_address = socket.gethostbyname(socket.gethostname())
    # print(f"my_ip_address: {my_ip_address}")
    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket info
    server_address = (my_ip_address, port)
    print('Start up on {} port {}'.format(*server_address))
    server_socket.bind(server_address)
    # activate socket
    server_socket.listen()
    print('accept wait')
    # listening..
    client_socket, client_address = server_socket.accept()
    while True:
        try:
            if data != prev_data:
                prev_data = data
                data = client_socket.recv(1024)
                data = pickle.loads(data)
                print("received data: ", end="")
                print(data)
                #######
                client_conversation_append(data)
                #######
        except Exception as err:  # 예외 발생 시
            print('Error:', err)

# send my text data to opponent server
def text_client(ip_address, port):
    print("text_client activated")
    import socket
    global data, prev_data
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip_address, port)
    client_socket.connect(server_address)
    # input value
    data = my.dialogue_for_opponent
    data = pickle.dumps(data)
    client_socket.send(data)