from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the local IP and port 12345
serverIP = '127.0.0.1'
serverPort = 12345
serverAddress = (serverIP, serverPort);
serverSocket.bind(serverAddress)

print('The server is ready to receive.')

while True:
    # Receive a byte string up to 2048 bytes long from the socket
    # The sender address is attached with the message
    messageBytes, clientAddress = serverSocket.recvfrom(2048)

    # Decode the byte string to a string object using the UTF-8 format
    message = messageBytes.decode("utf-8")

    try:
        elements = message.split(',')
        numbers = []
        for element in elements:
            numbers.append(int(element.strip()))

        product = 1
        for number in numbers:
            product = number * product

        reply = str(product)

    except:
        relpy = "Invalid input"
    

    # Send the product encoded in the UTF-8 format through the socket
    serverSocket.sendto(reply.encode("utf-8"), clientAddress)