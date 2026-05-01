import csv
import os

FILE_NAME = "data/students.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        os.makedirs("data", exist_ok=True)
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Course"])

def read_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        return list(reader)

def write_students(data):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Age", "Course"])
        writer.writerows(data)

def append_student(student):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(student.to_list())