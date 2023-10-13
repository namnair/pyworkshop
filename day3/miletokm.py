import tkinter as tk

def convert():
        miles = float(minput.get())
        km = miles * 1.60934
        kmlabel.config(text=f"{km:.2f} kilometers")
        

window = tk.Tk()
window.title("Miles to Kilometers Converter")

mlabel = tk.Label(window, text="Enter miles:")
mlabel.grid(row=0, column=0, padx=10, pady=10)

minput = tk.Entry(window)
minput.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(window, text="Convert", command=convert)
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

kmlabel = tk.Label(window, text="")
kmlabel.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
