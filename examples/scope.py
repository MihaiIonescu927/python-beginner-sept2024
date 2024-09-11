x = 100


def do_math(a, b):
    s = a + b
    print('inside func', x)
    return s, a - b, a * b, a // b


result = do_math(10, 20)
result2 = do_math(4, 6)

print('outside func', x)
