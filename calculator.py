from tkinter import *
from tkinter import font as tkfont

root = Tk()
root.title("Calculator")  

# font size for buttons and input box
large_font = tkfont.Font(size=20)  

root.geometry("502x580")  
root.resizable(False, False) 
root.config(bg="#1c1c1c")  # Background color 

# Input box
inputBox = Entry(root, borderwidth=5, width=30, fg="white", bg="#1c1c1c", font = large_font)
inputBox.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Global variable to store the current expression
expression = ""

# Function to handle button clicks and update the input box
def click(number):
    global expression
    if inputBox.get() == "Error!":  
        inputBox.delete(0, END)
        expression = ""
    expression += str(number)
    inputBox.delete(0, END)
    inputBox.insert(END, expression)

# Function to clear the input box and reset the expression
def backspace():
    global expression
    current_text = inputBox.get()
    if len(current_text) > 0:
        new_text = current_text[:-1]
        inputBox.delete(0, END)
        inputBox.insert(0, new_text)
        expression = new_text

# Function to evaluate the expression and display the result
def calculate():
    global expression
    try:
        result = eval(expression)
        inputBox.delete(0, END)
        inputBox.insert(0, result)
        expression = str(result)  
    except:
        inputBox.delete(0, END)
        inputBox.insert(0, "Error!")  
        expression = ""

# Functions to handle arithmetic operations
def add():
    click("+")

def sub():
    click("-")

def div():
    click("/")

def mul():
    click("*")

def equal():
    calculate()

# Function to handle keyboard input
def key_pressed(event):
    key = event.keysym
    if key in "0123456789":
        click(key)  #
    elif key == "minus":
        sub()  
    elif key == "plus":
        add()  
    elif key == "asterisk":
        mul()  
    elif key == "slash":
        div()  
    elif key == "period":
        click(".")  
    elif key == "equal" or key == "Return":
        equal()  
    elif key == "BackSpace":
        backspace() 
    elif key == "parenleft":
        click("(")  
    elif key == "parenright":
        click(")")  
root.bind("<Key>", key_pressed)

# buttons
Button(root, text="1", padx=40, pady=20, command=lambda: click("1"), fg="white", bg="#505050", font = large_font).grid(row=4, column=0, pady=2)
Button(root, text="2", padx=40, pady=20, command=lambda: click("2"), fg="white", bg="#505050", font = large_font).grid(row=4, column=1)
Button(root, text="3", padx=40, pady=20, command=lambda: click("3"), fg="white", bg="#505050", font = large_font).grid(row=4, column=2)

Button(root, text="4", padx=40, pady=20, command=lambda: click("4"), fg="white", bg="#505050", font = large_font).grid(row=3, column=0, pady=2)
Button(root, text="5", padx=40, pady=20, command=lambda: click("5"), fg="white", bg="#505050", font = large_font).grid(row=3, column=1)
Button(root, text="6", padx=40, pady=20, command=lambda: click("6"), fg="white", bg="#505050", font = large_font).grid(row=3, column=2)

Button(root, text="7", padx=40, pady=20, command=lambda: click("7"), fg="white", bg="#505050", font = large_font).grid(row=2, column=0, pady=2)
Button(root, text="8", padx=40, pady=20, command=lambda: click("8"), fg="white", bg="#505050", font = large_font).grid(row=2, column=1)
Button(root, text="9", padx=40, pady=20, command=lambda: click("9"), fg="white", bg="#505050", font = large_font).grid(row=2, column=2)

Button(root, text="0", padx=40, pady=20, command=lambda: click("0"), fg="white", bg="#505050", font = large_font).grid(row=5, column=0, pady=2)

# Special buttons
Button(root, text="<---", padx=26, pady=20, command=backspace, font = large_font, fg="white", bg="#D4D4D2").grid(row=1, column=0, pady=2)
Button(root, text="+", padx=39, pady=20, command=add, font = large_font, fg="white", bg="#ff9500").grid(row=4, column=3)
Button(root, text="-", padx=43, pady=20, command=sub, font = large_font, fg="white", bg="#ff9500").grid(row=3, column=3)
Button(root, text="*", padx=42, pady=20, command=mul, font = large_font, fg="white", bg="#ff9500").grid(row=2, column=3)
Button(root, text="/", padx=43, pady=20, command=div, font = large_font, fg="white", bg="#ff9500").grid(row=1, column=3)
Button(root, text=".", padx=52, pady=35, command=lambda: click("."), fg="white", bg="#505050").grid(row=5, column=1)
Button(root, text="=", padx=102, pady=20, command=equal, font = large_font, fg="white", bg="#ff9500").grid(row=5, column=2, columnspan=2)
Button(root, text="(", padx=43, pady=20, command=lambda: click("("), font = large_font, fg="white", bg="#D4D4D2").grid(row=1, column=1)
Button(root, text=")", padx=43, pady=20, command=lambda: click(")"), font = large_font, fg="white", bg="#D4D4D2").grid(row=1, column=2)


root.mainloop()
