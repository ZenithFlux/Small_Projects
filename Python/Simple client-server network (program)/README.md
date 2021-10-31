# Simple Client-Server Program

Very basic Client-Server chatting program.

This program is made to work with ngrok. Use ngrok to expose your localhost to the Internet so that server can listen to the connection request made by client. Ngrok is only required for the server pc only. 

## Steps make to this work

1. Tunnel ngrok 'tcp' server to port 50000 of server pc. (Don't use http server)

2. Put server address and port no. assigned by ngrok in respective fields in client.py (Remove 'tcp://' from address)

3. Run server.py first then client.py