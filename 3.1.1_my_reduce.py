import operator as op


def myreduce(func, obj, initial=None):
    if initial is None:
        val = obj[0]
        for i in obj[1:]:
            val = func(val, i)
    else:
        val = initial
        for i in obj:
            val = func(val, i)
    return val


print(myreduce(op.add, (1, 2, 3, 4, 5)))
print(myreduce(op.add, [1, 2, 3, 4, 5]))
print(myreduce(op.add, [1, 2, 3, 4, 5], 100))
print(myreduce(op.add, (), 5))
