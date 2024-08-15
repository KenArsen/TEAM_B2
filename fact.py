def factorial(a):
    total = 1
    for i in range(1, a + 1):
        total *= i
    print(total)


number = int(input())
factorial(number)
