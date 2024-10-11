import threading
import socket


HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
PORT = 4444

#get ip from hostname
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

#creates a socket with ipv4 and expects a stream of data
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bound this socket to this address
server.bind(ADDR)



#client to client comms

all_msgs = []
all_clients = []





def hand_client(conn, addr):
    print(f"New connection! {addr}")

    connected = True
    while connected:
        #manage bytes of message
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            all_msgs.append(msg)


            
            broadcast()


            #disconnect logic
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

        all_clients.append(conn)


        thread = threading.Thread(target=hand_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")



def broadcast():
    for c in all_clients:
        c.send(f"{all_msgs}".encode(FORMAT))






print("Server is STARTING!")
start()