from Tkinter import  *
import  tkinter.messagebox
root =  Tk()
#kinter.messagebox.showinfo("Window textile","venkatesh is a very good boy")

#answer=tkinter.messagebox.askquestion("Question 1","Do you like silly faces?")

#if answer== "yes":
#   print("silly ")
#canvas=Canvas(root,width=200,height=200)
#canvas.pack()
#blackline=canvas.create_line(0,0,200,50)
#redline=canvas.create_line(0,100,200,50,fill="red")
Photo= PhotoImage(file="vine-1948358_1280.png")
label=Label(root,image=Photo)
label.pack()

root.mainloop()