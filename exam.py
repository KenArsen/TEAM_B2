"""

Класс түзүү:
Person деген класс тузунуздор,
бул класста name жана age атрибуттары болуш керек.
Ошондой эле, бул класста introduce деген метод болсун,
ал "Hello, my name is {name} and I am {age} years old" деген созду чыргарсын.
Student деген классты тузунуздор,
ал Person классынан мурас алат жана кошумча student_id атрибутун кошунуздар.
Ошондой эле, study деген метод кошулсун,
ал "Student {name} is studying" деген созду чыграсын.

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f" hello, my name is: {self.name} and I am: {self.age} years old")
obj_1 = Person("Jyrgal", 20)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"my: {self.student_id}")
        super().introduce()
obj_2 = Student("jyrgal", 20, "2009-04-20")

obj_1.introduce()
obj_2.study()

