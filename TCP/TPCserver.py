from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode('utf-8')
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode("utf-8"))
    print('ResultTCP: ',capitalizedSentence)
    connectionSocket.close()