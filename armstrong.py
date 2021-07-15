def ARmstrong(num):
    sum = 0
    i= num
    order=len(str(num))
    while i> 0:
        digit = i% 10
        sum = sum+digit**order
        i=i// 10
    if num == sum:
        return num,"is an Armstrong number"
    else:
        return num,"is not an Armstrong number"
num = int(input("Enter a number"))
print(ARmstrong(num))