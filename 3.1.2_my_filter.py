def myfilter(func, obj):
    if func is None:
        for i in obj:
            if bool(i) is True:
                yield i
    else:
        for i in obj:
            yield func(i)


def square(a):
    return a * a


eg1 = filter(None, [1, 2, 3, 0, 4, 5, '0', (), 'string', [], 6])
eg2 = filter(square, [1, 2, 3, 4, 5])
print(eg1)
print(*list(eg1))
print(eg2)
print(*list(eg2))
