class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
            print(f'Name{self.name}')
            print(f'Age{self.age}')

animal = Animal('Baiel', '14')
animal.info()