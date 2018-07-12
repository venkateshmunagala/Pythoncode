from Tkinter import  *

class Venkatesh:
    def __init__(self,matter):
        frame = Frame(matter)
        frame.pack()
        self.Printbutton = Button(frame,text="print message",command=self.printmessage)
        self.Printbutton.pack(side=LEFT)
        self.quitButton = Button(frame,text="Quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printmessage(self):
        print("wow")

root = Tk()
venkat=Venkatesh(root)
root.mainloop()
