import tkinter
from tkinter import font
window=tkinter.Tk()
window.title("new")
window.minsize(500,300)

def print_hello():
    print("ok")
    
def print_input_data():
    data=float(input.get())
    sq=data**2
    label2.config(text=sq)
    
label1 = tkinter.Label(window, text="Enter: ")
label1.grid(row=1, column=1)
label2 = tkinter.Label(window, text="Display Square:")
label2.grid(row=4,column=3)
input=tkinter.Entry()
input.grid(row=1,column=3)
button = tkinter.Button(window, text="Click Me" , command=print_input_data)
button.grid(row=2, column=3)


window.mainloop()