import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasklist.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task = tasklist.curselection()[0]
        tasklist.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def complete_task():
    try:
        selected_task = tasklist.curselection()[0]
        tasklist.itemconfig(selected_task, {'bg':'light green', 'fg': 'gray'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

window = tk.Tk()
window.title("To-Do List Application")

tasklist = tk.Listbox(window, width=50)
tasklist.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

task_entry = tk.Entry(window, width=50)
task_entry.grid(row=1, column=0, padx=5, pady=5)

btnadd = tk.btnadd(window, text="Add Task", command=add_task)
btnadd.grid(row=1, column=1, padx=5, pady=5)

btnremove = tk.btnadd(window, text="Remove Task", command=remove_task)
btnremove.grid(row=2, column=0, padx=5, pady=5)

complete_btnadd = tk.btnadd(window, text="Complete Task", command=complete_task)
complete_btnadd.grid(row=2, column=1, padx=5, pady=5)

window.mainloop()
