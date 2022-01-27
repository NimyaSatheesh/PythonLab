# 5.Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character
x1 = str(input("Enter a string : "))
firstchar = x1[0]
x1 = x1.replace(firstchar, '$')
x1 = firstchar+x1[1:]
print(x1)
