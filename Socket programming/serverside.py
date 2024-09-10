import socket

# Server IP and port number
serverIP = '127.0.0.1'  # or the server's IP for remote use
port = 54321  # Replace '54321' with your desired port number

# Create a UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to an IP and port
serverSocket.bind((serverIP, port))

print(f"Server listening on {serverIP}:{port}")

while True:
    # Receive message from the client
    data, clientAddress = serverSocket.recvfrom(1024)
    print(f"Received message from {clientAddress}: {data.decode()}")

    # Send a reply to the client
    reply = "Message received"
    serverSocket.sendto(reply.encode(), clientAddress)
