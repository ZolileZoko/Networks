import socket

# Server IP and port number
serverIP = '127.0.0.1'  # This should match the server's IP address
port = 54321  # This should match the server's port number

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Input message from user
message = input('Input a message to send to the server providing your name: ')

# Send message to the server
clientSocket.sendto(message.encode(), (serverIP, port))

# Receive response from the server
response, serverAddress = clientSocket.recvfrom(1024)
print(f"Received response from server: {response.decode()}")

# Close the socket
clientSocket.close()
