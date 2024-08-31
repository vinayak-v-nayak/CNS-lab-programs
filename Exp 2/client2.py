import socket

# Define host and port
HOST = socket.gethostname()
PORT = 1234

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Receive data from the server
data = client_socket.recv(1024)

# Print the received message
print("Received message from server:", data.decode())

# Close the connection
client_socket.close()
