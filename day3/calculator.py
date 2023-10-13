import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def calculate():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

window = tk.Tk()
window.title("Basic Calculator")

display = tk.Entry(window, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)


buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=10, height=2, command=calculate).grid(row=row_val, column=col_val)
    elif button == "C":
        tk.Button(window, text=button, width=10, height=2, command=lambda b=button: display.delete(0, tk.END)).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, width=10, height=2, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()