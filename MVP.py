from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Minimum Viable Project')

#frames for the outcome
entry = Frame(root, background='#cee741')
base = Frame(root, background='blue')
sauce = Frame(root, background='#cee741')
cheese = Frame(root, background='#cee741')
toppings = Frame(root, background='#cee741')
finalise = Frame(root, background='#cee741')
confirm = Frame(root, background='#cee741')

#making the program open the frames in the full screen.
root.state("zoomed")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#adding frames to a list
frames = [entry, base, sauce, cheese, toppings, finalise, confirm]

#putting frames on the page
for frame in frames:
  frame.grid(row=0, column=0, sticky=NSEW)

#function for showing the frame on the screen
def show_frame(frame):
  frame.tkraise()

#making the entry screen appear first
show_frame(entry)

#-----Entry Screen Code-----#

#defining functions
def order():
  show_frame(base)

#make image variables
entryImage = ImageTk.PhotoImage(file="GizzaLogo.png")
orderLabel = ImageTk.PhotoImage(file="OrderButton.png")

#place on the screen
Label(entry, image=entryImage, borderwidth=0).pack(pady=100)
Button(entry, image=orderLabel, borderwidth=0, bd=5, command=order).pack(pady=0)

#-----Pizza View screen-----#
pizza = Frame(base, background='#cee741', height = 550, width = 550)
pizza.pack(anchor=NE)

def putOnPizza(img):
  label = Label(pizza, image=img)
  label.place(x=1,y=1)

Button(base, text="Gizza logo", command=lambda:putOnPizza(entryImage)).pack()
Button(base, text="Order buttton", command=lambda:putOnPizza(orderLabel)).pack()



root.mainloop()
