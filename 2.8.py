# Create a single string separated with space from two strings by swapping the character at position 1
print('Amal', 'Jyothi')
def string_exchange(a, b):
    exch_a = b[:2] + a[2:]
    exch_b = a[:2] + b[2:]
    return exch_a + exch_b


print(string_exchange('Amal', 'Jyothi'))
