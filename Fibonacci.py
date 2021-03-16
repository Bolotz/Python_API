
def Fibonacci(n):
    n = int(input('Provide n:' ))
    a = 0
    b = 1

    if n < 0:
        print("This input does not work with Fibonacci Sequence")

    elif n == 0:
        return 0

    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
    if b 
print(Fibonacci(9))