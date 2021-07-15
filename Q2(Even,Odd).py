def even_list(n):
    a=[]
    for i in n:
        if i%2==0:
            a.append(i)
    return a
print(even_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def even(a):
	i=0
	s= []
	while i<len(a):
		if a[i]%2==0:
			s.append(a[i])
		i= i+1
	print(s)
	
b=[1,2,3,4,5,6,7,8,9]
even(b)
#method
def check_number(a,b):
	if a%2==0 and b%2==0:
		print('even')
	else:
		print('even nhi hai')
check_number(20,12)
#question 5 ka part 1
def showNumber(n):
	i=0
	while i<=n:
		if i%2==0:
			print(i,"even")
		else:
			print(i,"odd")
		i=i+1
n=int(input("en"))
showNumber(n)
#find even odd
def even_odd(a):
    i=0
    even_1=[]
    odd_1=[]
    while i<len(a):
        if a[i]%2==0:
            even_1.append(a[i])
        else:
            odd_1.append(a[i])
        i+=1
    print(even_1)
    print(odd_1)

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,18,19,20]
def maximum(a):
    j=0
    m=0
    while j<len(a):
        s=0
        while s<len(a):
            if a[j]>a[s]:
                m=a[j]
            s+=1
        j+=1
    print(m)
maximum(a)
(even_odd(a))
def even_odd(a):
    i=0
    even_1=[]
    odd_1=[]
    while i<len(a):
        if a[i]%2==0:
            even_1.append(a[i])
        else:
            odd_1.append(a[i])
        i+=1
    print(even_1)
    print(odd_1)
    print(max(even_1))
    print(max(odd_1))
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17,18,19,20]
even_odd(a)