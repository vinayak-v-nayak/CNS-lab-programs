import socket
UDP_IP=socket.gethostname()
UDP_PORT=5005

print("Server hosted on:")
print("Host Name:", UDP_IP)
print("IP Address:", socket.gethostbyname(UDP_IP))
print("Port Number:", UDP_PORT)

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))
while True:
    data,addr=sock.recvfrom(1024)
    print("Recieved message:", data.decode())
    print("From:", addr)

    reply_message = "Thanks for the Message!"
    sock.sendto(reply_message.encode(), addr)

    # Receive reply from client
    reply_data, reply_addr = sock.recvfrom(1024)
    print("Client reply:", reply_data.decode())
