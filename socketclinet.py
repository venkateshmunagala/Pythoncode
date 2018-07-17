"""
__author__=venkatesh Munagala
__email__=venki.muna@gmail.com
 year =2018
"""
import  socket
import  threading
from tkinter import  *

def receive():
    """handles reecving message"""
    while True:
        try:
            msg=client.recv(1024).decode('utf8')
            msg_list.insert(END,msg)
        except OSError:
            break
def send(event=None):
    msg=my_msg.get()
    my_msg.set("")
    client.send(bytes(msg.encode('utf8')))
    if msg=="{quit}":
        client.close()
        root.quit
def closing(event=None):
    my_msg.set("{quit}")
    send()

root=Tk()
root.title('venkatesh chatting room')
#root.geometry()
messageframe=Frame(root)
my_msg=StringVar()
my_msg.set("Type here ")
scrollbar=Scrollbar(messageframe)
msg_list=Listbox(messageframe,height=40,width=70)
scrollbar.pack(side=RIGHT,fill=Y)
msg_list.pack(side=LEFT,fill=BOTH)
messageframe.pack()
entry_filed=Entry(root,textvariable=my_msg,)
entry_filed.bind("<Return>",send)
entry_filed.pack()
send_button=Button(root,text="send",command=send)
send_button.pack()
root.protocol("DELETE",closing)
host="192.168.0.10"
port=5000
buffersize=1024
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
receive=threading.Thread(target=receive)
receive.start()
root.mainloop()


