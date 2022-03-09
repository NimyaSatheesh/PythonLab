class rectangle():
	def __init__(self,breadth,length):
		self.breadth=breadth
		self.length=length
	def area(self):
		 return self.breadth*self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())
c=int(input('enter length of second rectangle'))
d=int(input('enter breadth of second rectangle'))
obj2=rectangle(c,d)
print('Area of rectangle',obj2.area())
if obj.area()==obj2.area():
	print('area are equal')
else:
	print('not equal')
