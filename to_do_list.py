import tkinter as tk
from tkinter import messagebox
import py_compile
import os

class ToDoList:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do List")

        # Frame for task list
        self.task_frame = tk.Frame(self.window)
        self.task_frame.pack(pady=10)

        # Task listbox with scrollbar
        self.task_listbox = tk.Listbox(self.task_frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, padx=10)
        self.scrollbar = tk.Scrollbar(self.task_frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        # Entry for adding new task
        self.task_entry = tk.Entry(self.window, width=50, font=("Arial", 12))  # تحديد خط النص
        self.task_entry.pack(pady=5)
        self.task_entry.bind("<Return>", self.add_task_enter)  # ربط الضغط على مفتاح Enter

        # Frame for buttons
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=5)

        # Add Task button
        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        # Delete Task button
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Protocol for window closing
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.tasks = []  # List to store tasks
        self.load_tasks()  # Load previously saved tasks
        self.update_task_listbox()  # Update task listbox

        self.window.mainloop()  # Start event loop

    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showerror("Error", "Task cannot be empty.")
            return
        self.tasks.append(task)
        self.update_task_listbox()
        self.save_tasks()  # Save tasks after adding
        self.task_entry.delete(0, tk.END)

    def add_task_enter(self, event):
        self.add_task()  # تنفيذ دالة إضافة المهمة عند الضغط على مفتاح Enter

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "No task selected.")
            return
        for index in selection[::-1]:
            self.tasks.pop(index)
        self.update_task_listbox()
        self.save_tasks()  # Save tasks after deletion

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        try:
            with open("tasks.txt", "w", encoding="utf-8") as file:  # تحديد الترميز UTF-8
                for task in self.tasks:
                    file.write(task + "\n")
            # Compile Python source files
            py_compile.compile("tasks.txt")
            # Remove the original source file
            os.remove("tasks.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {e}")

    def load_tasks(self):
        try:
            with open("tasks.pyc", "r", encoding="utf-8") as file:  # تحديد الترميز UTF-8
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {e}")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.save_tasks()  # Save tasks before closing
            self.window.destroy()

ToDoList()