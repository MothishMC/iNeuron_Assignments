print([i * j for i in ('x', 'y', 'z') for j in range(1, 5)])
print([i * j for i in range(1, 5) for j in ('x', 'y', 'z')])
print([[j] for i in range(2, 5) for j in range(i, i + 3)])
print([[j for j in range(i, i + 4)] for i in range(2, 6)])
print([(j, i) for i in range(1, 4) for j in range(1, 4)])
