import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Advanced To-Do List")
root.geometry("550x650")
root.configure(bg="#2C3E50")

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        del tasks[selected_task_index[0]]
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    if tasks:
        task_listbox.delete(0, tk.END)
        tasks.clear()
    else:
        messagebox.showinfo("Info", "No tasks to clear!")

def view_tasks():
    if tasks:
        tasks_str = "\n".join(tasks)
        messagebox.showinfo("Your Tasks", tasks_str)
    else:
        messagebox.showinfo("Info", "No tasks to display!")

tk.Label(root, text="To-Do List", font=("Arial", 26, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

task_frame = tk.Frame(root, bg="#34495E", padx=10, pady=10)
task_frame.pack(pady=10)

tk.Label(task_frame, text="Task Name:", font=("Arial", 14), bg="#34495E", fg="white").grid(row=0, column=0, padx=5, pady=5)
task_entry = tk.Entry(task_frame, font=("Arial", 14), width=30)
task_entry.grid(row=0, column=1, padx=5, pady=5)

task_listbox = tk.Listbox(root, font=("Arial", 12), width=50, height=12, bg="#ECF0F1")
task_listbox.pack(pady=10)

button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack()

tk.Button(button_frame, text="Add Task", font=("Arial", 14), bg="#27AE60", fg="white", width=12, command=add_task).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Delete Task", font=("Arial", 14), bg="#E74C3C", fg="white", width=12, command=delete_task).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Clear All", font=("Arial", 14), bg="#E67E22", fg="white", width=12, command=clear_tasks).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="View Tasks", font=("Arial", 14), bg="#3498DB", fg="white", width=12, command=view_tasks).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Exit", font=("Arial", 14), bg="#BDC3C7", fg="black", width=12, command=root.quit).pack(pady=10)

root.mainloop()
