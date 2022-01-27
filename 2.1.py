# (a) Generate positive list of numbers from a given list of integers
list1 = [1, -2, 3, -4, 5, 6, -7, 8, -9, 10]
print("list1 : ", list1)
print("Positive numbers : ")
for num in list1:
    if num >= 0:
        print(num)

# (b) Square of N numbers
list2 = [1, 2, 3, 4, 5, 34, 6, 78, 4, 8]
print("list1 : ", list2)
print("square of list1 : ")
for n in list2:
    print(n**2)

# (c) Form a list of vowels selected from a given word
n = input("Enter a word : ")
vowels = ['a', 'e', 'i', 'o', 'u']
list1 = []
for x in n:
    if x in vowels and x not in list1:
        list1.append(x)
print("vowels from list are  :", list1)

# (d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
a = input("Enter a word : ")
print("ordinal values : ")
list1 = []
for x in a:
    list1.append(ord(x))
print(list1)