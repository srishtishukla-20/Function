def nums(a):
	duplicate= []
	i= 0
	while i<len(a):
		if a[i] not in duplicate:
			duplicate.append(a[i])
		i= i+1
	print(duplicate)
b= [1,2,3,3,3,3,4,5]
nums(b)
#duplicate