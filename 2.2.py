list1 = []
limit = int(input("Enter limit:"))
for i in range(limit):
    a = int(input("Enter values:"))
    list1.append("Over" if a > 100 else a)
print(list1)
