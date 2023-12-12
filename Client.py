# UDPPingerServer.py
import random
import time
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets 
serverPort = 12000
serverAddress = ("10.44.210.189",serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP adddress and port number to socket
clientSocket.settimeout(1.0)

num = 1
rtt = []

for i in range(10):
    message = "Ping " + str(num)
    
    try:
        strt = time.time()
        
        clientSocket.sendto(message.encode(),(serverAddress))
        modified_message, serverAddress = clientSocket.recvfrom(2048)
        end = time.time()
        
        elapsed = end  - strt
        rtt.append(elapsed)
        
        print(modified_message.decode())
        print("Start Time: ", strt, " seconds")
        print("Return Time: ", end, " seconds")
        print("RTT: ", elapsed, " seconds")
        print()
        num = num+1

    except timeout:
        print("Ping " + str(num) + " request timed out")
        num = num+1
        print()

clientSocket.close()
