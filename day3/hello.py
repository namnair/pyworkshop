import tkinter 

window = tkinter.Tk()
window.title("Hello World!")

label = tkinter.Label(window, text="Hello World!")
label.pack(padx=20, pady=20)  

window.mainloop()
