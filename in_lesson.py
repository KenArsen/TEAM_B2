def info(a):
    s = 1
    for i in range(1, a + 1):
        s *= i
    print(s)


res = int(input())
info(res)