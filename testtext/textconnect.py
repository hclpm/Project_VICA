


def text_server(port):
    import socket
    # my current local ip address
    my_ip_address = socket.gethostbyname(socket.gethostname())
    print(f"my_ip_address: {my_ip_address}")
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
            # data receive (1024byte)
            data = client_socket.recv(1024)
            # decode received data
            data = data.decode()

            #######
            print('Received data:', data)
            #######
        except Exception as err:  # 예외 발생 시
            print('Error:', err)
        # if data == q // quit
        if data == "q":
            break
    client_socket.close()



def text_client(ip_address, port):
    import socket

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = ""
    server_address = (ip_address, port)

    # connect to socket
    client_socket.connect(server_address)

    while data != 'quit':
        try:
            # input value
            data = input("")
            data = data.encode()
            client_socket.send(data)
            # if data == 'quit' // quit
            if data == b'q':
                client_socket.close()
                break
        except Exception as e:
            print('Error:', e)