def showNumbers(limit):
    i=0
    while i<=limit:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i+=1
showNumbers(limit=int(input("enter number"))) 
#even and odd (Q.4 saral)
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
def functionname(a,b):
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
    else:
        print(a,b)
functionname("sonu","Khushi")
#print name which is greater in length
def functionName():
    quali="I have completed my graduation in B.Com"
    place="I am from Jharkhand"
    def function2():
        s="Hello"
        name="I am Srishti"
        print(s,"\n",name)
    function2()
    print(quali,"\n",place)
functionName()
#next line about yourself
def my_self(self):
	print(self)
my_self("hello")
my_self("my name is priyanka")
my_self("i am from jharkhand")
#About yourself in next next line
def greet(*names):
    i=0
    while i<len(names):
    	print("Hello", names[i])
    	i+=1
greet("sonu", "kartik", "umesh", "bijender")
#Q3.Saral
def my_function(a,b):
	a="Gouri"
	b="Priyanka"
	if len(a)<len(b):
		print(a+b+a)
	elif len(b)<len(a):
		print(b+a+b)
	else:
		pass
my_function(a="gouri",b="priyanka")
#print which has more length
def  greatername(a,b):
	i=0
	while i<len(b):
		if len(a)<len(b):
			print(a+b+a)
			break
		elif len(a)<len(b):
			print(b+a+b)
			break
		else:
			pass
		i+=1
greatername("gouri","srishti")
#another method
def eligible_for_vote():
	if age>=18:
		print('eligible for vote')
	else:
		print('not eligible for vote')
age= int(input('enter the age'))
eligible_for_vote()
# questions no. 1 from saral
