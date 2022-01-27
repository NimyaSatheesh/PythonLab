# Accept an integer n and compute n+nn+nnn
n = int(input("Enter a value n : "))
temp = str(n)
t1 = temp+temp
t2 = temp+temp+temp
compute = n+int(t1)+int(t2)
print("compute value = ", compute)
