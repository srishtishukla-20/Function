def HarshadNumber(num):
	sum= 0
	i= num
	while i>0:
		digit= i%10
		sum= sum+digit
		i= i//10
	if num%sum==0:
		return num,'is harshad no.'
	else:
		return num,' is not harshad no'
num= int(input('enter no.'))
print(HarshadNumber(num))