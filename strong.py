def Strongnum(n):
    a=n
    sum=0
    while n>0:
        i=1
        f=1
        b=n%10
        while i<=b:
            f=f*i
            i=i+1
        sum=sum+f
        n=n//10
    if a==sum:
        print("strong num")
    else:
        print("not strong num")
n=int(input("enter number"))
Strongnum(n)
#strongnum
