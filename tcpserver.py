import  socket
import  logging
from threading import  *
#from http.server import BaseHTTPRequestHandler
#from threading import  *

logging.basicConfig(filemode="file.txt",level=logging.INFO)

port = 9999
host = '192.168.0.10'
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((host,port))
skt.listen(10)
#skt.listen(5)
clients=[]
#skt.setblocking(0)
print("waiting for connection")





Quting=True
while Quting:
    client, addr = skt.accept()
    data=client.recv(1024).decode('utf8')
    if "Quit" in str(data):
        Quting=False

    if addr not in clients:
        clients.append(addr)

    print("received data :" +str(data))
    msg="Thanks"
    print(data)
    data=str(data).upper()
    client.send(bytes(data.encode('utf8')))
    client.close()


skt.close()







