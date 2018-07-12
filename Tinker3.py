from Tkinter import  *

def  Donothing():
    print("ok......................")

root = Tk()

#************Mennu*****************
matter = Menu(root)
root.config(menu=matter)

submenu = Menu(matter)
matter.add_cascade(label="File",menu=submenu) # this is having drop down functionality
submenu.add_command(label="New project",command=Donothing)
submenu.add_command(label="New ",command=Donothing)
submenu.add_separator()
submenu.add_command(label="exit ",command=quit)

editmenu = Menu(matter)
matter.add_cascade(label="edit",menu=editmenu)
editmenu.add_command(label="editing",command=quit)

# ********toolbar******************

toolbar = Frame( root, bg="blue")
insertButt =Button(toolbar,text="Insert images" ,command=Donothing)
insertButt.pack(side=LEFT,padx=2,pady=2)

printbutt=Button(toolbar,text="print",command=Donothing)
printbutt.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)

#************* status bar******************

status=Label(root,text="statusbar..............",bd=1,relief=SUNKEN,anchor=W)

status.pack(side=BOTTOM,fill=X)
root.mainloop()