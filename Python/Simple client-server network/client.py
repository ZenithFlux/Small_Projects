import socket

connection = socket.create_connection(('8.tcp.ngrok.io', 19935))

confirmation_msg = connection.recv(1024).decode()
if confirmation_msg != "":
    print(confirmation_msg)
else:
    print('Server is not active!')
    quit()

connection.sendall("Conncted with the client\nWaiting for Client\'s msg...".encode())

while True:
    msg = input("Your msg: ")
    if msg == "":
        msg = " "
    
    try:
        connection.sendall(msg.encode())
    except ConnectionAbortedError:
        print('Connection closed by the server!')
        break
    
    reply = connection.recv(1024).decode()
    if not reply == '':
        print("Server's msg: " + reply)
    else:
        print('Connection closed by the server!')
        break