def func(a, b):
   return a * b
a, b = map(int, input("введите цифры: ").split())
number = func(a, b)
print(number)