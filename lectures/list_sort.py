import random

a = range(100)

random.shuffle(a)

# Swap a[x] and a[y] if necessary so that they are in ascending order
# Assume that x < y
def compareAndSwap(a, x, y):
	pass

compareAndSwap(a, 0, 1)
compareAndSwap(a, 1, 2)
...

# How can you improve compareAndSwap so it only has two arguments