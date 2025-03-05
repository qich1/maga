def f(x, y):
    if x > y and x!=10:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y)

print(f(1, 25) * f(25, 28))