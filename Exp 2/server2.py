import socket

# Define host and port
HOST = socket.gethostname()
PORT = 1234

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((HOST, PORT))

# Get the actual port number
actual_port = server_socket.getsockname()[1]

# Listen for incoming connections
server_socket.listen(5)

print("Server is running on:")
print("Host Name:", HOST)
print("IP address:", socket.gethostbyname(HOST))
print("Port:", actual_port)

while True:
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address[0]}:{client_address[1]} has been established.")
    
    # Send a message back to client
    client_socket.sendall(b"Thanks for Connecting!")

    # Close the connection
    client_socket.close()
