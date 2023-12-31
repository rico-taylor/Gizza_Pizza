#Digital Technology Assessment 2023
#Function: Self Ordering System for Gizza Pizza
#Starting Date: 03/08/2023
#Date Last Modified: NOTE:chnage/NOTE:change/2023
#Coder: Rico Taylor

from tkinter import *
from PIL import ImageTk, Image
import re

root = Tk()
root.title('Minimum Viable Product')

#frames for the outcome
entry = Frame(root, background='#cee741')
base = Frame(root, background='blue')
sauce = Frame(root, background='blue')
cheese = Frame(root, background='blue')
toppings = Frame(root, background='blue')
finalise = Frame(root, background='#cee741')

#images for pizza
BaseClassic = ImageTk.PhotoImage(file="images/Base_wholemeal.png")
#BaseGlutenFree = ImageTk.PhotoImage(file="images/Base_GF.png")
#BaseThickCrust = ImageTk.PhotoImage(file="images/Base_thickCrust.png")
SauceTomato = ImageTk.PhotoImage(file="images/Sauce_pesto.png")
CheeseBasic = ImageTk.PhotoImage(file="images/Cheese_basic.png")
ToppingPepperoni = ImageTk.PhotoImage(file="images/Topping_mushroom.png")

#making the program open the frames in the full screen.
root.state("zoomed")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#adding frames to a list
frames = [entry, base, sauce, cheese, toppings, finalise]

#putting frames on the page
for frame in frames:
  frame.grid(row=0, column=0, sticky=NSEW)

#function for showing the frame on the screen
def show_frame(frame):
  frame.tkraise()

#-----Building screen of Pizza-----#
pizza = Frame(root, background='#cee741', height = 550, width = 550)
pizza.grid(row=0, column=0, sticky=NE)

#setting up a canvas in order to support png with transparent background
canvas = Canvas(pizza, bg="#cee741", width=550, height=550)
canvas.pack()

#defining the list that will be used for layering system
orderList = []

#function which sets out the list and then adds the images to the page
def putOnPizza(img, int, str):
  global orderList
  if img in orderList:
    pass
  else:
    if len(orderList) == 0:
      if int == 0:
        orderList.insert(0, int)
        orderList.insert(1, img)
        orderList.insert(2, str)
    elif orderList[-3] < int:
      orderList.append(int)
      orderList.append(img)
      orderList.append(str)
    elif int not in orderList:
      numb = int
      while numb not in orderList:
        numb -= 1
        if numb in orderList:
          lower = numb
          orderList.insert(orderList.index(lower) + 3, int)
          orderList.insert(orderList.index(lower) + 4, img)
          orderList.insert(orderList.index(lower) + 5, str)
    else:
      for x in orderList:
        if x == int:
          orderList.insert(orderList.index(x) + 3, int)
          orderList.insert(orderList.index(x) + 4, img)
          orderList.insert(orderList.index(x) + 5, str)
          break
        else:
          pass
    for item in orderList:
      if (orderList.index(item) -1) % 3 == 0:
        canvas.create_image(275,275, image=item)

Button(base, text="Base", command=lambda:putOnPizza(BaseClassic, 0, "Classic Base")).grid(row=1, column=4)
#Button(base, text="Base", command=lambda:putOnPizza(BaseGlutenFree, 0, "Gluten Free Base")).grid(row=2, column=4)
#Button(base, text="Base", command=lambda:putOnPizza(BaseThickCrust, 0, "Thick Crusted Base")).grid(row=3, column=4)
Button(sauce, text="Sauce", command=lambda:putOnPizza(SauceTomato, 1, "Tomato Sauce")).grid(row=1, column=4)
Button(cheese, text="Cheese", command=lambda:putOnPizza(CheeseBasic, 2, "Basic Cheese")).grid(row=1, column=4)
Button(toppings, text="Topping", command=lambda:putOnPizza(ToppingPepperoni, 3, "Pepperoni")).grid(row=1, column=4)

#-----Base Screen Code-----#
def BASE():
  global stages
  global last_screen
  last_screen = BASE
  stages = base
  show_frame(stages)
  pizza.place(x=1366,y=0)
  show_frame(pizza)
  pagesBar()
  goToFinal()
#-----Sauce Screen Code-----#
def SAUCE():
  global stages
  global last_screen
  last_screen = SAUCE
  stages = sauce
  show_frame(stages)
  pizza.place(x=1366,y=0)
  show_frame(pizza)
  pagesBar()
  goToFinal()
#-----Cheese Screen Code-----#
def CHEESE():
  global stages
  global last_screen
  last_screen = CHEESE
  stages = cheese
  show_frame(stages)
  pizza.place(x=1366,y=0)
  show_frame(pizza)
  pagesBar()
  goToFinal()
#-----Toppings Screen Code-----#
def TOPPING():
  global stages
  global last_screen
  last_screen = TOPPING
  stages = toppings
  show_frame(stages)
  pizza.place(x=1366,y=0)
  show_frame(pizza)
  pagesBar()
  goToFinal()

#-----Overarching Screen code-----#
def pagesBar():
  global stages
  icon = Label(stages, image=entryImage, borderwidth=0) #change the size later of the image itself
  goToBase = Button(stages, text="BASE", command=BASE)
  goToSauce = Button(stages, text="SAUCE", command=SAUCE)
  goToCheese = Button(stages, text="CHEESE", command=CHEESE)
  goToToppings = Button(stages, text="TOPPING", command=TOPPING)

  goTo = [icon, goToBase, goToSauce, goToCheese, goToToppings]

  for x in goTo:
    x.grid(row=0, column=goTo.index(x), pady=35, padx=5)

#-----Entry Screen Code-----#

#make image variables
entryImage = ImageTk.PhotoImage(file="images/GizzaLogo.png")
orderLabel = ImageTk.PhotoImage(file="images/OrderButton.png")

#place on the screen
Label(entry, image=entryImage, borderwidth=0).pack(pady=100)
Button(entry, image=orderLabel, borderwidth=0, bd=5, command=BASE).pack(pady=0)

#-----Finalise Order Screen-----#

#defining functions
def final():
  global orderList
  global finalise
  global orderList
  show_frame(finalise)
  pizza.place(x=30,y=150)
  show_frame(pizza)
  Label(finalise, text="Your Pizza:").grid(row=1, column=1, padx=350, pady=10, sticky=W)
  nameList = []
  Label(finalise, height=19, width=1000, bg="#cee741").place(x=618,y=232)
  for item in orderList:
    if (orderList.index(item) + 1) % 3 == 0:
      nameList.append(item)
  for name in nameList:
    Label(finalise, text=name, bg="#cee741").grid(row=(2+nameList.index(name)), column=1, padx=350, pady=5, sticky=W)

enterName = Label(finalise, text="Enter your name:").place(x=620, y=630)
userName = Entry(finalise, width=50)
userName.place(x=620, y=660)


def confirm():
  global names
  global finish
  names = userName.get()
  userName.delete(0 ,'end')
  individualNames = names.split()
  errorIntegers = Label(finalise, text="error: only letters allowed", background='#cee741', fg="red")
  Integer = False
  for x in individualNames:
    x.capitalize()
    if not re.match("^[A-z]*$", x): #if the name isn't a letter from a-z the computer will ask the user again for their input
      Integer = True
      errorIntegers.place(x=690, y=695)
  if individualNames == []:
    Label(finalise, text="                                                ", background='#cee741').place(x=690, y=695)
    Label(finalise, text="error: no name", background='#cee741', fg="red").place(x=690, y=695)
  elif Integer == False:
    Label(finalise, text="                                                ", background='#cee741').place(x=690, y=695)
    name = []
    for x in names.split():
      name.append(x.capitalize())
    finish = Toplevel(width=250, height=100, background='#cee741')
    finish.title('Confirmation')
    finish.grab_set()
    Label(finish, text=name).grid(row=0,column=0, padx=10)
    Label(finish, text="Would you like to confirm your order?", bg='#cee741').grid(row=1, column=0, columnspan=2, padx=10)
    Button(finish, text="Yes", command=yes).grid(row=2, column=0, padx=2)
    Button(finish, text="No", command=no).grid(row=2, column=1)

def yes():
  global finish
  global orderList
  global canvas
  finish.destroy()
  message = Toplevel(width=250, height=100, background='#cee741')
  Label(message, text="Your order will be ready to pick up in store in ten minutes", bg='#cee741').pack(padx=20, pady=10)
  Label(message, text="Thankyou for buying from Gizza Pizza", bg='#cee741').pack(padx=20)
  orderList = []
  canvas.delete("all")
  show_frame(entry)

def no():
  final()
  finish.destroy()

Button(finalise, text="Proceed", command=confirm).place(x=620, y=690)

def goToFinal():
  Button(stages, text="finalise order", command=final).grid(row=5, column=4)
  Button(finalise, text="back to ording", command=last_screen).grid(row=0, column=0, padx=80, pady=80)

#-----Main Routine-----#

#making the entry screen appear first
show_frame(entry)

root.mainloop()