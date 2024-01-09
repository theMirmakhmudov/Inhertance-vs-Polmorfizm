class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Ismi:{self.name}\nYoshi:{self.age}"


class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def student_info(self):
        return f"Ismi:{self.name}\nYoshi:{self.age}\nId:{self.id}"


student_obj = Student("Abdulmajid", 15, 123)
print(student_obj.student_info())
