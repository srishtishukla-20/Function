def perfect(n):
   sum = 0
   i=1
   while i<n:
            	if n%i==0:
            		sum += i
            	i+=1
   return sum == n
number = int(input('Enter number: '))
if perfect(number):
    print(number,"is perfect number")
else:
    print(number,"is not perfect number")
  #perfect number
def perfect_number(n):
    sum=0
    i=1
    while i<n:
        if n%i==0:
            sum = sum + i
        i=i+1
    if (sum == n):
        print(n," is a Perfect number!")
    else:
        print(n," is not a Perfect number!")
n =int(input("Enter any number: "))
perfect_number(n)