def divisibal5():
	a=[60,75,15,55,10,2,88]
	i=0
	b=[]
	while i<len(a):
		if a[i]%5==0:
			b.append(a[i])
		i+=1
	return b
c=divisibal5()
def greater50(c):
	j=0
	while j<len(c):
		if c[j]>50:
				print(c[j])
		j+=1
print(c)
greater50(c)
#Calling one function to another

def multiples_of_5():
	a=[50,60,15,66,65,85,89,99,5,10]
	i=0
	list=[]
	while i<len(a):
		if a[i]%5==0:
			list.append(a[i])
		i+=1
	return list
c=multiples_of_5()
def greater_than_50(c):
	j=0
	list2=[]
	while j<len(c):
		if c[j]>=50:
			list2.append(c[j])
		j+=1
	print(list2)
	return c
print(greater_than_50(c))
#multiples of 5 and greater than 50

def divisiable_of_5():
	a=[15,5,10,12,13,14]
	i=0
	list=[]
	while i<len(a):
		if a[i]%5==0:
			list.append(a[i])
		i+=1
	return list
c=divisiable_of_5()
def greater_than_10(e):
	j=0
	list2=[]
	while j<len(e):
		if e[j]>=10:
			list2.append(e[j])
		j+=1
	print(list2)
greater_than_10(c)
#output=[10,15]