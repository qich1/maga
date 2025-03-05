def f(x, y):
    if x > y and x!=12:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 3, y)

print(f(4, 6) * f(6, 50))