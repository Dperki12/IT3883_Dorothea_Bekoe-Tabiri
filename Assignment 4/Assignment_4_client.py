# Program Name: Assignment_4_client.py
# Course: IT3883/Section 01/W02
# Student Name: Dorothea Bekoe-Tabiri
# Assignment Number: Lab#4
# Due Date: 03/24/2025
# Purpose: Client py file that will prompt the user to type in a string & send to server.
# List Specific resources used to complete the assignment: W3Schools, Stack Overflow, personal Python projects

import socket

host = '127.77.77.77'  # localhost
port = 50000  # Must match server port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# get message from user and send it
string = input("Message to server: ")
s.send(string.encode())  # turn to bytes

# wait for response
reply = s.recv(1024)
print("Server said:", reply.decode())

# close
input("Press enter to exit.")
s.close()
