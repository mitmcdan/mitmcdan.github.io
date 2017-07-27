#Michael McDaniel
from tkinter import *
import random
#Section 1
##This is just laying out all of the buttons and labels
#Section 3
##This is the functioning radio buttons for width and color
class Application(Frame):
    patternList = []
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lblS = Label(self, text = "Roman Numeral Canvas")
        self.lblS.grid(row = 0, column = 0, columnspan = 3, sticky = N)
        self.canvas = Canvas(self, height=310, width = 500)
        self.canvas.grid(row = 1, column = 0, rowspan = 6, columnspan = 1)
        self.lblW = Label(self, text = "Number: ")
        self.lblW.grid(row = 1, column = 1, sticky = E)
        self.entry1 = Entry(self, width = 30)
        self.entry1.grid(row = 1, column = 2, columnspan = 2, sticky = W)
        self.num = BooleanVar()
        self.check1 = Checkbutton(self, text = "Numbers", variable = self.num)
        self.check1.grid(row = 1, column = 4)
        self.color = StringVar()
        self.color.set("Black")
        self.width = StringVar()
        self.width.set("1")
        self.lblE = Label(self, text = "Line Width: ")
        self.lblE.grid(row = 2, column = 1, sticky = E)
        self.radio1 = Radiobutton(self, text = "1", variable = self.width, value = "1")
        self.radio1.grid(row = 2, column = 2, sticky = S)
        self.radio2 = Radiobutton(self, text = "3", variable = self.width, value = "3")
        self.radio2.grid(row = 2, column = 3, sticky = S)
        self.radio3 = Radiobutton(self, text = "5", variable = self.width, value = "5")
        self.radio3.grid(row = 2, column = 4, sticky = S)
        self.lblL = Label(self, text = "Line Color: ")
        self.lblL.grid(row = 3, column = 1, sticky = E)
        self.radio4 = Radiobutton(self, text = "Black", variable = self.color, value = "Black")
        self.radio4.grid(row = 3, column = 2, sticky = S)
        self.radio5 = Radiobutton(self, text = "Red", variable = self.color, value = "Red")
        self.radio5.grid(row = 3, column = 3, sticky = S)
        self.radio6 = Radiobutton(self, text = "Blue", variable = self.color, value = "Blue")
        self.radio6.grid(row = 3, column = 4, sticky = S)
        self.romanPic = PhotoImage(file="roman.gif")
        self.randomPic = PhotoImage(file="random.gif")
        self.btn1 = Button(self, image = self.romanPic, command = self.roman)
        self.btn1.grid(row = 4, column = 2, sticky = W)
        self.btn2 = Button(self, image = self.randomPic, command = self.random)
        self.btn2.grid(row = 4, column = 4, sticky = W)
        self.colorList = ['Black', 'Red', 'Blue', 'Green']
        self.widthList = ['1','2', '3','4', '5']
#Section 2
##This will be assigning commands to the buttons, getting the input of letters, then tracing out those
##letters with create_line many times over
        self.x, self.y = 20, 20
        
    def roman(self):
        self.widthSet = int(self.width.get())
        self.number = self.entry1.get()
        self.colorSet = self.color.get()
        for letter in self.number:
            if letter == "M":
                self.M()
            elif letter == "D":
                self.D()
            elif letter == "C":
                self.C()
            elif letter == "I":
                self.I()
            elif letter == "L":
                self.L()
            elif letter == "X":
                self.X()
            elif letter == "V":
                self.V()
    def D(self):
        self.canvas.create_line(self.x, self.y, self.x + 15, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 15, self.y, self.x + 27, self.y + 12, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 27, self.y + 12, self.x + 27, self.y + 32, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 27, self.y + 32, self.x + 15, self.y + 44, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x, self.y + 44, self.x + 16, self.y + 44, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x, self.y, self.x, self.y + 44, width = self.widthSet, fill = self.colorSet)
        self.lineJump()
    def C(self):
        self.canvas.create_line(self.x, self.y + 7, self.x + 7, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 7, self.y, self.x + 20, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x, self.y + 7, self.x, self.y + 35, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 7, self.y + 42, self.x + 20, self.y+ 42, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x, self.y + 35, self.x + 7, self.y + 42, width = self.widthSet, fill = self.colorSet)
        self.lineJump()
    def I(self):
        self.canvas.create_line(self.x, self.y, self.x + 10, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 4, self.y, self.x + 4, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x, self.y + 40, self.x + 10, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.lineJump()
    def L(self):
        self.canvas.create_line(self.x, self.y, self.x + 7, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 3, self.y, self.x + 3, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x, self.y + 40, self.x + 17, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.lineJump()
    def X(self):
        self.canvas.create_line(self.x, self.y, self.x + 15, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x, self.y + 40, self.x + 15, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x - 4, self.y, self.x + 20, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x - 3, self.y + 40, self.x + 20, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.lineJump()
            
    def V(self):
        self.canvas.create_line(self.x, self.y, self.x + 8, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 8, self.y + 40, self.x + 16, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x - 4, self.y, self.x + 20, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x - 3, self.y + 40, self.x + 20, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.lineJump()
    def lineJump(self):
        if self.x >= 460:
            self.x = 20
            self.y += 50
        else:
            self.x += 30
    def M(self):
        self.canvas.create_line(self.x, self.y, self.x + 7, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 3, self.y, self.x + 3, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x, self.y + 40, self.x + 7, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 3, self.y, self.x + 13, self.y + 10, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 13, self.y + 10, self.x + 23, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 20, self.y, self.x + 26, self.y, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 23, self.y, self.x + 23, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.canvas.create_line(self.x + 20, self.y + 40, self.x + 26, self.y + 40, width = self.widthSet, fill = self.colorSet)
        self.lineJump()
#Section 4 Bonus
##This will need to recall the correct letter function through roman but each letter changes the width and color
##This would require each of the if statements above to be turned into functions then pass it a new width and color
    def random(self):
        for letter in self.number:
            if letter == "M":
                self.colorSet = random.choice(self.colorList)
                self.widthSet = random.choice(self.widthList)
                self.M()
            elif letter == "D":
                self.colorSet = random.choice(self.colorList)
                self.widthSet = random.choice(self.widthList)
                self.D()
            elif letter == "C":
                self.colorSet = random.choice(self.colorList)
                self.widthSet = random.choice(self.widthList)
                self.C()
            elif letter == "I":
                self.colorSet = random.choice(self.colorList)
                self.widthSet = random.choice(self.widthList)
                self.I()
            elif letter == "L":
                self.colorSet = random.choice(self.colorList)
                self.widthSet = random.choice(self.widthList)
                self.L()
            elif letter == "X":
                self.colorSet = random.choice(self.colorList)
                self.widthSet = random.choice(self.widthList)
                self.X()
            elif letter == "V":
                self.colorSet = random.choice(self.colorList)
                self.widthSet = random.choice(self.widthList)
                self.V()
#Section 5 Bonus would have been setting that input number equal to total, then % that total until it hits 0 and have multiple if statements to check
#whether the mod macthes any of the options and continue until it hits zero, too bad I ran out of time.
# main
root = Tk()
root.title("Roman Numerals")
root.geometry("900x350")

app = Application(root)
root.mainloop()

#I really enjoyed this class, I have learned alot thanks to all of you guys, Thanks!

