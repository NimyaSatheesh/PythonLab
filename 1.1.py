#Display future leap years from current year to a final year entered by user.
a = int(input("current year  : "))
b = int(input("Final year  : "))
for i in range(a, b):
    if(i%4==0):
        print(i)
