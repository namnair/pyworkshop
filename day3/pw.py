import tkinter as tk
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pwgenerate():
    l = int(entry_letters.get())
    s = int(entry_symbols.get())
    nn = int(entry_numbers.get())

    pw = []
    for _ in range(0, l):
        pw += random.choice(letters)

    for _ in range(0, s):
        pw += random.choice(symbols)

    for _ in range(0, nn):
        pw += random.choice(numbers)

    random.shuffle(pw)

    password = ""
    for char in pw:
        password += char

    password_display.config(text=f"Your newly generated password is: {password}")


window = tk.Tk()
window.title("Password Generator")


tk.Label(window, text="How many letters would you like in your password?").pack()
entry_letters = tk.Entry(window)
entry_letters.pack()

tk.Label(window, text="How many symbols would you like?").pack()
entry_symbols = tk.Entry(window)
entry_symbols.pack()

tk.Label(window, text="How many numbers would you like?").pack()
entry_numbers = tk.Entry(window)
entry_numbers.pack()

generate_button = tk.Button(window, text="Generate Password", command=pwgenerate)
generate_button.pack()

password_display = tk.Label(window, text="")
password_display.pack()


window.mainloop()
