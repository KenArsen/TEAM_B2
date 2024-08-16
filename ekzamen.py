class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
person = Person('baiel',14)
person.introduce()

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
    def studi(self):
        print(f'Student {self.name} is studying')
rp = Student('Arsen',22,'2010')
rp.studi()