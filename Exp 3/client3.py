import socket

UDP_IP = socket.gethostname()
UDP_PORT = 5005
MESSAGE = "Welcome to Computer Network Lab!!!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("Message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Encode the message to bytes before sending
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

# Receive data from the server
reply, addr = sock.recvfrom(1024)
print("Server:", reply.decode())

# Send reply back to server
reply_message = "Thank you for connecting!"
sock.sendto(reply_message.encode(), (UDP_IP, UDP_PORT))

# Close the socket
sock.close()
