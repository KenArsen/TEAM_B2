def factor(a):
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    print(fact)
nurlis = int(input())
factor(nurlis)