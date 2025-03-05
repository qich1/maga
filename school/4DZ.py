def f(x, y):
    if x > y and x!=12:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x * 2, y)

print(f(2, 20) * f(20, 30))