def list(n):
	i=0
	#n=int(input("en"))
	c=1
	sum=0
	empty=[]
	while i<n:
		j=0
		list=[]
		while j<n:
			list.append(c)
			sum+=c
			c+=1
			j+=1
		i+=1
		print(sum)
		empty.append(list)
	print(empty)

n=int(input("en"))
list(n)
#add and make nested list
def sum(n):
	i=0
	sum=0
	while i<=n:
		if i%3==0 or i%5==0:
			sum+=i
		i=i+1
	print(sum)
n=int(input("en"))
sum(n)
#sum
def sum(a,b,c):
	sum=0
	sum=a+b+c
	avg=sum/3
	print(sum)
	print(avg)
a=int(input("en"))
b=int(input("en"))
c=int(input("en"))
sum(a,b,c)
#Avg ,sum in function
def sumavrg(num):
    i=0
    sum=0
    while i<num:
        num1=int(input("enter any number1="))
        sum+=num1
        i+=1
    average=sum/num
    print(sum)
    print(average)
num=int(input("enter="))
sumavrg(num)
#sum and avrg from user input(saral Q.3)
def collect(a,b):
	i=0
	e=[]
	c=a+b
	while i<len(c):
		if c[i] not in e:
			e.append(c[i])
		i+=1
	e.sort()
	print(e)
a= [1, 5, 10, 12, 16, 20]
b= [1, 2, 10, 13, 16] 
collect(a,b)
#add  two list
def add(a):
	i=0
	new=0
	list=[]
	while i<len(a):
		new=a[i]+new
		list.append(new)
		i+=1
	print(list)
a=[1,2,3,5,6]
add(a)
#sum of numbers in function