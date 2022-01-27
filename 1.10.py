# Create a string from given string where first and last characters exchanged.
str1 = input("Enter a string :")
exch_string = str1[-1]+str1[1:-1]+str1[0]
print(exch_string)