class Student:
    def __init__(self, student_id, name, age, course):
        self.id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_list(self):
        return [self.id, self.name, self.age, self.course]