class bank:
	def __init__(self,a,n,t,b):
		self.acc=a
		self.name=n
		self.type=t
		self.bal=b
	def deposit(self,a):
		self.bal+=a
		print(self.bal)
	def withdraw(self,a):
		self.bal-=a
		print(self.bal)
a=int(input("enter the account number"))
n=input("enter tyhe name ")
t=input("enter the type of account")
b=int(input("enter the balance amount"))
obj=bank(a,n,t,b)
d=int(input("enter the amount to deposit"))
obj.deposit(d)
w=int(input("enter the amount to withdraw"))
obj.withdraw(w)