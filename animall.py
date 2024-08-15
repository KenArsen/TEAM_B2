class Animall:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"name is: {self.name} \n Age is: {self.age}")
obj = Animall("Bob", 2)
obj.info()


