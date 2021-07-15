def sqr(n):
	i=1
	while i<=n:
		dic[i]=i*i
		i=i+1
n=int(input("en"))
dic={}
sqr(n)
print(dic)