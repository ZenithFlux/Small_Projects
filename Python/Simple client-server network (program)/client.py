import socket

connection = socket.create_connection(('Server address', 16557)) #Put ngrok Server Address and port number here

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