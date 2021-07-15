def threeLargest(list):
	i=0
	largest1=0
	largest2=0
	largest3=0
	while i<len(list):
		if list[i]>largest1:
			largest1=list[i]
			j=0
			while j<len((list)):
				if (largest1>list[j] and largest2<list[j]):
					largest2=list[j]
					e=0
					while e<len(list):
						if largest2>list[e] and largest3<list[e]:
							largest3=list[e]
						e+=1
				j+=1
		i+=1
	return  "First maximum is:",largest1, "2nd maximum is:",largest2,"3rd maximum is:",largest3
list=[3,6,7,8,1,11,45,6,89,10]
print(threeLargest(list))
#first 3 maximum using function