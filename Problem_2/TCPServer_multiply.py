from socket import *

# Create a TCP welcoming socket
welcomeSocket = socket(AF_INET, SOCK_STREAM)

# Bind it to the local IP and port 12345
serverIP = '127.0.0.1'
serverPort = 12345
serverAddress = (serverIP, serverPort)
welcomeSocket.bind(serverAddress)

# Welcome socket begins listening for incoming TCP requests
# Allows up to 1 pending requests for connection in the queue
welcomeSocket.listen(1)
print('The server is ready to receive')

while True:
    
    # Server waits on accept() for incoming requests
    # A new connection socket is created on return
    connectionSocket, clientAddress = welcomeSocket.accept()
    clientIP, clientPort = clientAddress

    # Receive a byte string from the connection socket
    messageBytes = connectionSocket.recv(1024)
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

    except ValueError:
        relpy = "Invalid input"


    # Send a byte string to the connection socket
    connectionSocket.sendall(reply.encode("utf-8"))

    # Close the connection socket to this client
    connectionSocket.close()
    # The welcoming socket is still open for new clients
