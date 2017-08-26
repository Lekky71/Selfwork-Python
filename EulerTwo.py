def __fib__(n):
    if n == 0:
        return 0, 1
    else:
        a, b = __fib__(n / 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return c, d
        else:
            return d, d + c


def __fibonacci__(n):
    if n < 0:
        raise ValueError("no negatives")
    else:
        return __fib__(n)[0]


total = 0
num = 2
while total <= 4000000:
    if __fibonacci__(num) % 2 == 0:
        total += __fibonacci__(num)
    num = num + 1
print total
