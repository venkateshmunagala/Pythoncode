import  sys
import  socket
import  select

HOST=''
PORT=4096
SOCKET_LIST=[]
REC_BUFFER=1024
def chatserver():
    connnection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connnection.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    connnection.bind((HOST,PORT))
    connnection.listen(10)
    SOCKET_LIST.append(connnection)
    print("chat is started at port {}".format(PORT))
    while True:
        read,write,error=select.select(SOCKET_LIST,[],[],0)
        for soc in read:
            if soc==connnection:
                socad,adrres=connnection.accept()
                SOCKET_LIST.append(socad)
                print("client {} is connected".format(adrres))
                broadcast(connnection,socad,"{} joined the chatting room".format(adrres))
            else:
                """ process data from received """
                try:
                    data=



def broadcast(connection,socad,msg):
    for sockets in SOCKET_LIST:
        if sockets!=connection and sockets!=socad:
            try:
                sockets.send(msg)
            except:
                sockets.close()
                if sockets in SOCKET_LIST:
                    SOCKET_LIST.remove(sockets)



chatserver()