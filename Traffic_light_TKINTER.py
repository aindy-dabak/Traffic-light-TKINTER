from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame

def do_button_press():
    """The window managet will call this function when the user
       presses the graphical  button.
       The variables color,canvas, red_lamp,yellow_lamp,
       and green_lamp are global variables that this function
       expects to exist.
       Since we assign only to the color variable, it is the only
       variable that needs explicit global declaration."""
    global color
    if color == 'red':
        color = 'yellow'
        canvas.itemconfigure(red_lamp, fill='black')       #Turn red off
        canvas.itemconfigure(yellow_lamp, fill='yellow')     #Turn green on
    elif color == 'green':
        color = 'red'
        canvas.itemconfigure(green_lamp, fill='black')      #Turn green off
        canvas.itemconfigure(red_lamp, fill='red')    #Turn yellow on
    elif color == 'yellow':
        color = 'green'
        canvas.itemconfigure(yellow_lamp, fill='black')      #Turn yellow off
        canvas.itemconfigure(green_lamp, fill='green')           #Turn red on


#Create and initialize global variables
color = 'red'   #The lights current color
root = Tk()     #Create the graphical window
root.title("Traffic Light")

frame = Frame(root)  #Create a frame to hold the widgets
frame.pack()         #Make the frame fill the entire window


#Create a drawing surface within the frame
canvas = Canvas(frame, width=150,height=300)

#Set up the visual aspects of the traffic light
#Traffic light Frame
canvas.create_rectangle(50,20,150,280, fill='gray')

red_lamp = canvas.create_oval(70,40,130,100, fill='red')
yellow_lamp = canvas.create_oval(70,120,130,180, fill='black')
green_lamp = canvas.create_oval(70,200,130,260,fill='black')

button = Button(frame, text ='Change Traffic Light', command=do_button_press)

button.grid(row=0,column=0)
canvas.grid(row=0,column=1)

root.mainloop()


