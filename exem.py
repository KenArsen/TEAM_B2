class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello {self.name} and i am {self.age} years old")


ob1 = Person('Bilal', 14)
ob1.introduce()


class Student(Person):
    def __init__(self, student_id):
        self.student_id = student_id
        super().__init__(name, age)

    def study(self):
        print(f"Student {self.name} is studing")


ob2 = Student("09,10,11")
ob2.study()
