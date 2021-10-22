import socket

s = socket.create_server(('localhost', 50000))

connection, address = s.accept()

connection.sendall('Connected with server'.encode())
print(connection.recv(1024).decode())


while True:
    try:
        reply = connection.recv(1024).decode()
        if not reply == '':
            print("Client's msg: " + reply)
        else:
            print('Disconnected from client!')
            break
    except ConnectionAbortedError:
        print('Disconnected from client!')
        break
    
    msg = input("Your msg: ")
    if msg == "":
        msg = " "
    connection.sendall(msg.encode())