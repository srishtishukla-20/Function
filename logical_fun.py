def mul(numbers):
    total = 1
    x=0
    while x<len(numbers):
        total *= numbers[x]
        x+=1
    return total
print(mul([8, 2, 3, -1, 7]))
#multiples
def Reverse(a):
    str1=" "
    j=len(a)
    while j>0:
        str1=str1+a[j-1]
        j-=1
    return str1
print(Reverse("1234abc"))
#reverse of string
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
#factorial number
def test(a):
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add
func= test(4)
print(func(4))
#one fun to another
total={}
def insert(items):
    if items in total:
        total[items] += 1
    else:
        total[items] = 1
insert('Apple')
insert('Ball')
insert('Apple')
print (len(total))
#insert
def speed(s):
    d = 0
    if s==75 and s % 5 == 0:
        d += ((s-75) / 5) + 1
        print("Demrit points:",d)
        if d >= 12:
            print("license suspended")
s=int(input("enter num"))
speed(s)
#speed
def sum_of_multiples(limit):
    count = 1
    sum = 0
    multiples = []
    while count <= limit:
        if count % 3 == 0 and count not in multiples:
            multiples.append(count)
            print(count)
        elif count % 5 == 0 and count not in multiples:
            multiples.append(count)
            print(count)
        count+=1
        for each in multiples:
            sum +=each
    print("\nSum is " + str(sum))
limit = int(input("Enter the limit: "))
sum_of_multiples(limit)