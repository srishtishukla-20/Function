def find(a):
	i=0
	upper=0
	lower=0
	while i<len(a):
	         	if a[i]>='a' and a[i]<='z':
	         		lower+=1
	         	if a[i]>='A' and a[i]<='Z':
	         		upper+=1
	         	i+=1
	print("No. of upper case letters:",upper)
	print("No. of lower case letters:", lower)
find(a="The quick Brown Fox")
#number of upper and lower case