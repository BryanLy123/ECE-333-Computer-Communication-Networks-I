#ECE 333 Project 3
#Lab 3: SMTP Lab
#Authors: Bryan Ly, Armando Moreno, Fash Fasogbon
#April 10, 2023

from socket import *
from base64 import *
import ssl

userEmail = "ece333temp3@gmail.com" #burner Gmail account
userDestEmail = "ece333temp3@gmail.com"
userPassword = "szedmpyvmquqdwuw" #apps password via Google Account
userID = "Project_SMTP" #Temporary Email Subject

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
port = 587 #Gmail port number
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
  print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
 print('250 reply not received from server.')
 
initCMD = "STARTTLS\r\n".encode()
clientSocket.send(initCMD)
recv2 = clientSocket.recv(1024)

clientSocket_SSL = ssl.wrap_socket(clientSocket)

mailE = b64encode(userEmail.encode()) #email username encoding
mailP = b64encode(userPassword.encode()) #email passworkd encoding

authorizeCMD = "Authorize Login\r\n" #login authorization

clientSocket_SSL.send(authorizeCMD.encode())
recv2 = clientSocket_SSL.recv(1024)
print(recv2)

clientSocket_SSL.send(mailE + "\r\n".encode())
recv3 = clientSocket_SSL.recv(1024)
print(recv3)

clientSocket_SSL.send(mailP + "\r\n".encode())
recv4 = clientSocket_SSL.recv(1024)
print(recv4)

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <{}>\r\n".format(userDestEmail)
clientSocket_SSL.send(mailFrom.encode())
recv5 = clientSocket_SSL.recv(1024)
print(recv5)
if recv5[:3] != '250':
  print('250 reply not received from server.')

#Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <{}>\r\n".format(userDestEmail)
clientSocket_SSL.send(mailFrom.encode())
recv5 = clientSocket_SSL.recv(1024)
print(recv5)
if recv5[:3] != '250':
  print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <{}>\r\n".format(userDestEmail)
clientSocket_SSL.send(rcptTo.encode())
recv6 = clientSocket_SSL.recv(1024)
print(recv6)
if recv6[:3] != '250':
  print('250 reply not received from server.')

# Send DATA command and print server response.
dataCMD = 'DATA\r\n'
clientSocket_SSL.send(dataCMD.encode())
recv7 = clientSocket_SSL.recv(1024)
print(recv7)
if recv7[:3] != '354':
  print('354 reply not received from server.')

# Send message data.
clientSocket_SSL.send("Subject: {}\n\n{}".format(userID, msg).encode())

# Message ends with a single period.
clientSocket_SSL.send(endmsg.encode())
recv8 = clientSocket_SSL.recv(1024)
print(recv8)
if recv8[:3] != '250':
  print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
quitCMD = 'QUIT\r\n'
clientSocket_SSL.send(quitCMD.encode())
recv9 = clientSocket_SSL.recv(1024)
print(recv9)
if recv9[:3] != '221':
  print('221 reply not received from server.')

#Close the socket.
clientSocket_SSL.close()