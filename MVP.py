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

#images for pizza
BaseClassic = ImageTk.PhotoImage(file="images/Base_classic.png")
SauceTomato = ImageTk.PhotoImage(file="images/Sauce_tomato.png")
CheeseBasic = ImageTk.PhotoImage(file="images/Cheese_basic.png")
ToppingPepperoni = ImageTk.PhotoImage(file="images/Topping_pepperoni.png")

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
entryImage = ImageTk.PhotoImage(file="images/GizzaLogo.png")
orderLabel = ImageTk.PhotoImage(file="images/OrderButton.png")

#place on the screen
Label(entry, image=entryImage, borderwidth=0).pack(pady=100)
Button(entry, image=orderLabel, borderwidth=0, bd=5, command=order).pack(pady=0)

#-----Pizza View screen-----#
pizza = Frame(base, background='#cee741', height = 550, width = 550)
pizza.pack(anchor=NE)

#setting up a canvas in order to support png with transparent background
canvas = Canvas(pizza, bg="#cee741", width=550, height=550)
canvas.pack()

orderList = []

def putOnPizza(img, int):
  global orderList
  print(str(img))
  if len(orderList) == 0:
    if int == 0:
      orderList.insert(0, int)
      orderList.insert(1, str(img))
  elif orderList[-2] < int:
    orderList.append(int)
    orderList.append(str(img))
  elif int not in orderList:
    numb = int
    while numb not in orderList:
      numb -= 1
      if numb in orderList:
        lower = numb
    orderList.insert(lower + 2, int)
    orderList.insert(lower + 3, str(img))
  else:
    for x in orderList:
      if x == int:
        orderList.insert(orderList.index(x) + 2, int)
        orderList.insert(orderList.index(x) + 3, str(img))
        break
      else:
        pass
  print(orderList)
  if len(orderList) == 0 and int != 0:
    pass
  else:
    canvas.create_image(275, 275, image=img)


Button(base, text="Base", command=lambda:putOnPizza(BaseClassic, 0)).pack()
Button(base, text="Sauce", command=lambda:putOnPizza(SauceTomato, 1)).pack()
Button(base, text="Cheese", command=lambda:putOnPizza(CheeseBasic, 2)).pack()
Button(base, text="Topping", command=lambda:putOnPizza(ToppingPepperoni, 3)).pack()



#note for next time: I need to make a list, then this list will keep track of what is on the screen at any time. I also need to make a dictionary. This will give each one an attribute for the order that it needs to go. Then when another option is picked it can be swapped out for the thing in the list with the same attribute/order number.

root.mainloop()
