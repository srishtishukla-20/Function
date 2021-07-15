def l(List):
    Sum = 0
    for i in List:
        Sum = Sum + i
    return Sum

print(l([1,3,5,7,9]))
#sum hackathon
def driver(speed):
	speed1=speed-70
	point=speed1//5
	if speed<=70:
		print("ok")
	elif point>12:
		print("license suspended")
	elif speed>70:
		print(point,"point")
speed=int(input("enter speed "))
driver(speed)
#speed
def l():
    list = []
    i=1
    while i<=10:
       list.append(i)
       i=i+1
    return list
a = l()
print(a)
#append 10 numbers in list
def multiply(numbers):  
    s = 1
    for x in numbers:
        s *= x  
    return s  
print(multiply((8, 2,7)))
#multiply
