#ECE 333
#Web Server

#import socket module
from socket import *
import time
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 7242
#Fill in end

#Establish the connection
serverSocket.bind(("",serverPort)) 
#binds the serverSocket to specific IP and port number
serverSocket.listen(1) #readiness to accept client content

while True:
  print('Ready to serve...')
  connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
  
  try:
    message = connectionSocket.recv(1024).decode()#Fill in start #Fill in end
    filename = message.split()[1]
    f = open(filename[1:])
    outputdata = f.read()#Fill in start #Fill in end
    #Send one HTTP header line into socket
    #Fill in start
    connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
    connectionSocket.send("Content-Type: text/html\r\n".encode())
    connectionSocket.send(message.encode())
    #Fill in end
    #Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
      connectionSocket.send(outputdata[i].encode())
      
    connectionSocket.send("\r\n".encode())
    connectionSocket.close()
    
  except IOError:
  #Send response message for file not found
  #Fill in start
    print("404 Not Found!")
    connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\n".encode())
    connectionSocket.close()
  #Fill in end
  #Close client socket
  #Fill in start
  #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
