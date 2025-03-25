# Program Name: Assignment_4_server.py
# Course: IT3883/Section 01/W02
# Student Name: Dorothea Bekoe-Tabiri
# Assignment Number: Lab#4
# Due Date: 03/24/2025
# Purpose: Server file that listens for string from client.Receive & convert it to all upper case, and send it back.
# List Specific resources used to complete the assignment: W3Schools, Stack Overflow, personal Python projects

import socket  # needed for network stuff

# setup info
host = '127.77.77.77'  # same computer
port = 50000  # make sure client uses same port

# make server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

print("Server is LISTENING...")

con, addy = s.accept()  # wait for client
print("Connected to:", addy)

# message to client
info = con.recv(1024)

# get message
if info:
    data = info.decode()
    print("Received:", data)
    # make all caps
    reply = data.upper()
    con.send(reply.encode())

    # send it back
    print("Response:", reply)

# pause before closing
input("Press Enter to exit.")
s.close()
