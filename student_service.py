from models.student import Student
from utils.file_handler import read_students, write_students, append_student

def add_student(student):
    append_student(student)

def get_all_students():
    return read_students()

def delete_student(selected):
    students = read_students()
    updated = [s for s in students if s != selected]
    write_students(updated)

def update_student(old_data, new_student):
    students = read_students()
    updated = []

    for s in students:
        if s == old_data:
            updated.append(new_student.to_list())
        else:
            updated.append(s)

    write_students(updated)