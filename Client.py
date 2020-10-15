import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "192.168.1.4"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    message_len = len(message)
    send_len = str(message_len).encode(FORMAT)
    send_len += b' ' * (HEADER - message_len)
    client.send(send_len)
    client.send(message)

online = True

while online:
    message = input("> ")
    
    if message == "disc!":
        send(DISCONNECT_MSG)
        online = False
    else:
        send(message)
print("[DISCONNECTED!]")

