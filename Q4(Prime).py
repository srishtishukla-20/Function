def prime_num(n):
    i=1
    counter=0
    while i<=n:
        if n%i==0:
            counter+=1
        i+=1
    if counter==2:
        print("prime number")
    else:
        print("not prime number")
n=int(input("enter the num"))
prime_num(n)
#prime num
def prime(num):
    i=2
    x=0
    while i>0:
        j=1
        count=0
        while j<i:
            if i%j==0:
                count+=1
            j+=1
        if count==1:
            print(i,"prime no")
            x+=1
        if x==num:
            break
        i+=1
prime(num=int(input("enter any num=")))
#another method
