from socket import  *
from threading import  *

def connections():
    """ handlig connections"""
    while True:
        global    client
        client,adrees=s.accept()

        print("{} has connected".format(address))
        client.send(bytes("welcome to cave! type your name and adrees",'utf8'))
        adr[client]=address
        Thread(target=handle_clinet,args=(client,)).start()
def handle_clinet(client):
    name=client.recv(1024).decode('utf8')
    welcome=" welcome {} if you want to quit type {quit} ",format(name)

    msg=" name joined the chat"
    broadcast(bytes(msg,'utf-8'))
    clients[client]=name
    while True:
        msg=client.recv(1024)
        if msg!=bytes("{quit},{utf-8}"):
            broadcast(msg,name+":")

def broadcast(msg,prefix=""):
    for sock in clients:
        sock.send(bytes(prefix,msg))

clients={}
adr={}

host="192.168.0.10"
port=5000
buffersize=1024
address=(host,port)
s=socket(AF_INET,SOCK_STREAM)
s.bind(address)

s.listen(5)
print("waiting for connections ")
Accept_thread=Thread(target=connections)
Accept_thread.start()
Accept_thread.join()
s.close()
