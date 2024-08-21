def isalmak_a():
    salmak = boi - 110
    print("сиздин идеалдуу салмак", salmak, "кг")

def isalmak_e():
    salmak = boi - 100
    print("сиздин идеалдуу салмак", salmak, "кг")

boi = int(input("боюнуздун узундугун см менен киргизиниз: "))
j = input("жынысыз a/э: ")
if j == "а":
    isalmak_a()
elif j == "э":
    isalmak_e()

