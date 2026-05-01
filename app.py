import tkinter as tk
from tkinter import messagebox
from models.student import Student
from services.student_service import *

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        self.id_entry = tk.Entry(root)
        self.name_entry = tk.Entry(root)
        self.age_entry = tk.Entry(root)
        self.course_entry = tk.Entry(root)

        tk.Label(root, text="ID").pack()
        self.id_entry.pack()

        tk.Label(root, text="Name").pack()
        self.name_entry.pack()

        tk.Label(root, text="Age").pack()
        self.age_entry.pack()

        tk.Label(root, text="Course").pack()
        self.course_entry.pack()

        tk.Button(root, text="Add", command=self.add).pack()
        tk.Button(root, text="Update", command=self.update).pack()
        tk.Button(root, text="Delete", command=self.delete).pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.select)

        self.selected_data = None
        self.refresh()

    def add(self):
        student = Student(
            self.id_entry.get(),
            self.name_entry.get(),
            self.age_entry.get(),
            self.course_entry.get()
        )
        add_student(student)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for s in get_all_students():
            self.listbox.insert(tk.END, s)

    def select(self, event):
        selected = self.listbox.curselection()
        if selected:
            self.selected_data = self.listbox.get(selected)

    def delete(self):
        if self.selected_data:
            delete_student(list(self.selected_data))
            self.refresh()

    def update(self):
        if self.selected_data:
            new_student = Student(
                self.id_entry.get(),
                self.name_entry.get(),
                self.age_entry.get(),
                self.course_entry.get()
            )
            update_student(list(self.selected_data), new_student)
            self.refresh()