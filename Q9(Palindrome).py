def palindrome(a):
	if a==a[::-1]:
		print('it is palindrome')
	else:
		print('it is not palindrome')
palindrome(a=(input('enter the name')))