import  socket
import  logging

logging.basicConfig(filemode="venkates.txt",level=logging.INFO)


def Main():
    #host='localhost'



    #server='192.168.0.20', 9999


    while True:
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        s.connect((host, port))
        message = input("enter some data:")
        s.send(bytes(message.encode('utf8')))
        data=s.recv(1024,).decode('utf8')
        print("data received from servr:",str(data))
    #    message = input("enter some data:")
    s.close()
Main()

