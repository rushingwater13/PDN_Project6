from socket import *

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# The destination is specified by a tuple of IP and port
serverIP = '127.0.0.1'
serverPort = 12345
serverAddress = (serverIP, serverPort);

# Input a message and encode it to a byte string in the UTF-8 format
message = input('Input a list of comma-separated numbers:')
messageBytes = message.encode("utf-8")

# Send a message through the client socket
clientSocket.sendto(messageBytes, serverAddress)

# Receive a byte string up to 2048 bytes long from the client socket
# The sender information is attached with the message
modifiedMessageBytes, serverAddress = clientSocket.recvfrom(2048)
modifiedMessage = modifiedMessageBytes.decode("utf-8")

print(f'Product = {modifiedMessage}')

clientSocket.close()
