import threading
import socket


HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 5050

#get ip from hostname
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

#creates a socket with ipv4 and expects a stream of data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bound this socket to this address
server.bind(ADDR)

def hand_client(conn, addr):
    print(f"New connection! {addr}")

    connected = True
    while connected:
        #manage bytes of message
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"{addr}, {msg}")
            conn.send(f"Message Recieved! {msg}".encode(FORMAT))

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"{addr} disconnected!")
            
            
    
    conn.close()


def start():
    server.listen()
    print(f"Server is LISTENING on {ADDR}")
    while True:
        #stores client connections in tuple
        conn, addr = server.accept()
        thread = threading.Thread(target=hand_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")



print("Server is STARTING!")
start()