import socket

s = socket.socket()
s.bind(('localhost', 80))
print('Server running...')

while True:
    s.listen()
    connection, address = s.accept()
    
    request = connection.recv(4096).decode()
    
    if request.startswith('GET /'):
        
        with open('site.html', 'r') as f:
            site = f.read()
            
            response = 'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n' + site
            connection.sendall(response.encode())
        
    connection.close()