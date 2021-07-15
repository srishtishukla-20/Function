def multiple_list(a,b):
	i=0
	list1=[]
	while i<len(a):
		j=a[i]*b[i]
		list1.append(j)
		i+=1
	print(list1)
multiple_list([5,10,50,20],[2,20,3,5])
#Q.6 part2 saral
def multiples(limit):
    i=0
    sum=0
    while i<=limit:
        if i%3==0:
            sum=sum+i
        if i%5==0:
            sum=sum+i
        
        i+=1
    print(sum)    
multiples(limit=int(input("enter number")))
#Q.5 SARAL
