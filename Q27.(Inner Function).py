def function1(n):
	def function2():
		print(n**2)
	function2()
function1(n=int(input("enter number")))
#inner function
def test(a):
	def add(b):
		nonlocal a
		a=a+1
		return a+b
	return add
fun=test(4)
print(fun(4))
#inside function
def myFunction(a):
	b=a
a=input("enter name")
def greet(j):
	b=j
	return b
print(greet(j=a))
#inner function call