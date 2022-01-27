# print out all colors from color-list1 not contained in color-list2
color_list1 = set(["Black", "Green", "Blue", "White"])
color_list2 = set(["Red", "Orange", "Black", " White"])
print("color-list1 not contained in color-list2 are : ")
print(color_list1.difference(color_list2))
