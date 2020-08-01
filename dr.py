import random
import tkinter
from PIL import ImageTk, Image

class die():
    def __init__(self,ivalue,parent):
        self.label_var = tkinter.IntVar()
        self.label_var.set(ivalue)
        self.display = tkinter.Label(parent,relief='ridge', borderwidth=4,
                                              textvariable=self.label_var)
        self.display.pack(side='left')

    def roll(self):
            value = random.randint(1,6)
            self.label_var.set(value)
            print ("You rolled =  ", value)

def rollin():
    d1.roll()
    d2.roll()
    d3.roll()

if __name__=="__main__":
    win = tkinter.Tk()
    win.title("Die Roller")
    row1 = tkinter.Frame(win)
    row2 = tkinter.Frame(win)
    d1 = die(1,row1)
    d2 = die(1,row1)
    d3 = die(1,row1)
    #### above d1,d2,d3 can be changed according to your dice needed
    row1.pack()
    rolldice = tkinter.Button(row2, command=rollin, text = "Roll The Die")
    rolldice.pack()
    row2.pack()
    ##img = ImageTk.PhotoImage(Image.open("meme.jpg"))
    ###panel =tkinter.Label(win, image =  img)
    ##panel.pack(side = "bottom", fill = "both", expand = "yes")
    win.mainloop()
