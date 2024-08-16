class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Name: {self.name}')
        print((f'Age: {self.age}'))

pr = Animal('cat',4)


pr.info()