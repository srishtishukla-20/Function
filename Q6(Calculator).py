def calculator(a,b):
	symbol=input("enter symbol ")
	if symbol=="+":
		print(a+b)
	elif symbol=="-":
		print(a-b)
	elif symbol=="*":
		print(a*b)
	elif symbol=="/":
		print(a/b)
	elif symbol=="//":
		print(a//b)
	else:
		print("nothing")
calculator(45,35)
#1st method
def add(a,b):
    sum=a+b
    return sum
def subl(c,d):
    subl=c-d
    return subl
def mul(e,f):
    mul=e*f
    return mul
def div(g,h):
    div=g%h
    return div
print(add(20,25))
print(subl(40,3))
print(mul(10,4))
print(div(40,4))
#2nd method
def calculator(number1,number2):
    c=[]
    i=0
    mult=0
    while i<len(number1):
        mult=(number1[i]*number2[i])
        c.append(mult)
        i=i+1
    print(c)
calculator(number1=[5,10,50,20],number2=[2,20,3,5])
# 3rd method
def calculator(a,b):
	if symbol=="+":
		return (a+b)
	if symbol=="-":
		return (a-b)
	if symbol=="*":
		return (a*b)
	if symbol=="/":
		return (a/b)
	if symbol=="//":
		return (a//b)
	else:
		return ("nothing")
#symbol=input(('enter symbol'))
a= int(input('enter the first no.'))
b= int(input('enter the second no.'))
symbol=input(('enter symbol'))
print(calculator(a,b))
#4th method

