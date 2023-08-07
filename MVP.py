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

#-----Building screen of Pizza-----#
stages = base #change this depending on what screen the screen is in at the time

pizza = Frame(stages, background='#cee741', height = 550, width = 550)
pizza.pack(anchor=NE)

#setting up a canvas in order to support png with transparent background
canvas = Canvas(pizza, bg="#cee741", width=550, height=550)
canvas.pack()

#defining the list that will be used for layering system
orderList = []

#function which sets out the list and then adds the images to the page
def putOnPizza(img, int):
  global orderList
  if img in orderList:
    pass
  else:
    if len(orderList) == 0:
      if int == 0:
        orderList.insert(0, int)
        orderList.insert(1, img)
    elif orderList[-2] < int:
      orderList.append(int)
      orderList.append(img)
    elif int not in orderList:
      numb = int
      while numb not in orderList:
        numb -= 1
        if numb in orderList:
          lower = numb
          orderList.insert(orderList.index(lower) + 2, int)
          orderList.insert(orderList.index(lower) + 3, img)
    else:
      for x in orderList:
        if x == int:
          orderList.insert(orderList.index(x) + 2, int)
          orderList.insert(orderList.index(x) + 3, img)
          break
        else:
          pass
    for item in orderList:
      if orderList.index(item) % 2 != 0:
        canvas.create_image(275,275, image=item)

Button(base, text="Base", command=lambda:putOnPizza(BaseClassic, 0)).pack()
Button(base, text="Sauce", command=lambda:putOnPizza(SauceTomato, 1)).pack()
Button(base, text="Cheese", command=lambda:putOnPizza(CheeseBasic, 2)).pack()
Button(base, text="Topping", command=lambda:putOnPizza(ToppingPepperoni, 3)).pack()

#-----Base Screen Code-----#
def BASE():
  global stages
  show_frame(base)
  stages = base
#-----Sauce Screen Code-----#
def SAUCE():
  global stages
  show_frame(sauce)
  stages = sauce
#-----Cheese Screen Code-----#
def CHEESE():
  global stages
  show_frame(cheese)
  stages = cheese
#-----Toppings Screen Code-----#
def TOPPING():
  global stages
  show_frame(toppings)
  stages = toppings

#-----Overarching Screen code-----#
goToBase = Button(stages, text="BASE", command=BASE)
goToBase = Button(stages, text="SAUCE", command=SAUCE)
goToBase = Button(stages, text="CHEESE", command=CHEESE)
goToBase = Button(stages, text="TOPPING", command=TOPPING)

#-----Entry Screen Code-----#

#make image variables
entryImage = ImageTk.PhotoImage(file="images/GizzaLogo.png")
orderLabel = ImageTk.PhotoImage(file="images/OrderButton.png")

#place on the screen
Label(entry, image=entryImage, borderwidth=0).pack(pady=100)
Button(entry, image=orderLabel, borderwidth=0, bd=5, command=BASE).pack(pady=0)




#-----Finalise Order Screen-----#

#defining functions

def back():
  show_frame(base)

def final():
  show_frame(finalise)

#NOTE: Change the frame that the buttons are in from base to whatever they need to be in
Button(base, text="finalise order", command=final).pack(anchor=SE)
Button(finalise, text="back to ording", command=back).pack()

root.mainloop()