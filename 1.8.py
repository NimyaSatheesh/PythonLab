# From a list of integers, create a list removing even numbers.
a = [0, 2, 3, 4, 5, 67, 6, 8, 9, 29, 39]
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
print(b)
