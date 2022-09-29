import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
ip_port = ('127.0.0.1',25565)
sock.bind(ip_port)
sock.listen(5)

while True:
    conn,address = sock.accept()
    send_data = 'Hello.'
    conn.sendall(send_data)
    while True:
        try:
            recv_data = conn.recv(1024)
            if recv_data[0:5] == 'start':
                print ('Ok, Starting...')
                pass   
            if recv_data[0:4] == 'exit':
                break
        except Exception as e:
            break
    conn.close()