
from socket import *
serverName = 'LAPTOP-KJ3KB4S4' #192.168.52.78 LAPTOP-KJ3KB4S4
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode('utf-8'),(serverName,serverPort ))
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

