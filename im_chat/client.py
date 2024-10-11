import socket


HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 4444
SERVER = "192.168.1.176"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect():
    client.connect(ADDR)

def send(msg):
    
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
def client_rec():
    msg_list = client.recv(2048).decode(FORMAT)
    msg_list = msg_list.replace("'", "")
    msg_list = msg_list.replace('[', "")
    msg_list = msg_list.replace(']', "")



    msg_list = msg_list.split(",")
    print(type(msg_list))
    return msg_list