#Find biggest of 3 numbers entered.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a>b and a>c:
    print("first number is greatest number")
elif b>c and b>a:
    print("second number is greatest")
elif c>a and c>b:
    print("third number  is greatest")
else:
    print("not defined....!")