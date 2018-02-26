def genfibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        t = a
        a = b
        b = t+b

for num in genfibon(10):
    print num
