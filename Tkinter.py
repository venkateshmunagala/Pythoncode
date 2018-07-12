from tkinter import  *

root = Tk()
"""
#thelable=Label(root,text="This is chwy bot")
#thelable.pack()
#topframe=Frame(root)
#topframe.pack(side=TOP)
#bottomframe=Frame(root)
#bottomframe.pack(side=BOTTOM)
#button1=Button(topframe,text="EOBXML",fg="red")
#button2=Button(bottomframe,text="XML",fg="blue")

#button1.pack(side=LEFT)
#button2.pack(side=LEFT)

#one=Label(root,text="This is a chwy bot",fg="red",bg="blue")
#one.pack()
#two=Label(root,text="this is chwy one",fg="blue",bg="white")
#two.pack(fill=X)
#label_1=Label(root,text="name")
#label_2=Label(root,text="password")
#Entry1=Entry(root)
#Entry2=Entry(root)
#label_1.grid(row=0,sticky=E)
#label_2.grid(row=1,sticky=E)
#Entry1.grid(row=0,column=1)
#Entry2.grid(row=1,column=1)
#c = Checkbutton(root,text="Keep log in")
#c.grid(columnspan=2)
#def printname(event):
  #  print("helo my name is venkatesh")

#utton1=Button(root,text="print name")
#button1.bind("<Button->",printname)
#button1.pack()
"""


def leftclick(event):
    print("left")


def middleclick(event):
    print("middle click")


def rightclick  (event):
    print("right click")
frame = Frame(root, width= 300, height=250)
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("Button-3>", rightclick)
frame.pack()
root.mainloop()


