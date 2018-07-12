from  tkinter import  *
from random import  *
window=Tk()
window.title("Geometry")
window.configure(background="Blue")
window.geometry("400x400")
#-------------------------------Funtion --------------------------#
def functime():
    phrase=["hello","hi","whatsup"]

    name=str(entry.get())

    return  phrase[randint(0,2)]+name

def greeting():
    value=functime()
    data2=str(entry.get())
    display=Text(window,height=10,width=30)
    display.grid(column=3,row=3)
    display.delete(0.0,END)
    display.insert(END,value)
    #try:
    #      data=dictonary[data2]
    #except:
    #    print("data is not present")
    #display.insert(END,data)
    #display['state']="disabled"

#----------------Images --------------------------------#
#Photo=PhotoImage(file="vine-1948358_1280.png")
#label=Label(window,image=Photo)
#label.pack()


#--------creating a label--------------#
lable=Label(window,text="My new label:")
lable.grid(column=0,row=0,sticky=E)
label=Label(window,text="what is your name?",bg="blue",font="none 12 bold",fg="white")
label.grid(column=0,row=1)

#-------------Entries----------------#
entry=Entry(window,width=20)
entry.grid(column=1,row=1,sticky=NE)

#------------------Button-----------------#
button=Button(text='my new button',command=greeting,bg="red")
button.grid(column=1,row=2)
#-------------dictonary -------------------------#
dictonary={"Bug":"we invented a bug in the program"}

window.mainloop()