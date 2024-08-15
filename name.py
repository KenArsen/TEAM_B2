def info(width, height, perimetr = True):
   if perimetr:
      return width + height * 2
   else:
      return width * height

a, b = map(int, input(" ").split())

rez = info(a, b, False)
print("ayant: ", rez)




