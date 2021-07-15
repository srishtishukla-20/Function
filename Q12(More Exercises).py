def num():
	i=1
	while i<=1000:
		if i%3==0:
		    print(i,"nav")
		if i%7==0:
			print(i,"gurukul")
		if i%21==0:
			print(i,"navgurukul")
		else:
			pass
		i+=1
num()
#more exercises of function
def expenses_numberOfStudents(a,b):
	if a*b<=50000:
		return "hum budget ke ander hai"
	if a*b>50000:
		return "hum budget ke bahar hai"
	else:
		pass
a=int(input("enter number of students"))
b=int(input("enter expenses"))
print(expenses_numberOfStudents(a,b))
#saral Q.2 more exercises
def greatest(a,b,c):
	if a>b and a>c:
		return a,"is greatest"
	if b>a and b>c:
		return b,"is greatest"
	if c>a and c>b:
		return c,"is greatest"
	else:
		return "all are equal"
a=int(input("enter number1"))
b=int(input("enter number2"))
c=int(input("enter number3"))
print(greatest(a,b,c))
#Q.4 saral more exercises
def check(string_list):
	i=0
	list=[]
	while i<len(string_list):
		if string_list[i] not in list:
			list.append(string_list[i])
		else:
			pass
		i+=1
	print(list)
string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
check(string_list)
#Q.6 Saral more exercises
def common_elements(list1,list2):
	new_list = []
	i=0
	while i<len(list1):
			if list1[i] in list2:
				new_list.append(list1[i])
			i+=1
	return new_list
list1=[1, 342, 75, 23, 98]
list2=[75, 23, 98, 12, 78, 10, 1] 
print(common_elements(list1,list2))
#Q.7 saral more exercises
def common_elements(list1,list2):
	new_list = []

	i=0
	while i<len(list1)-1:
			if list1[i] in list2:
				new_list.append(list1[i])
			if list1[i] not in list2:
				new_list.append(list1[i])
			if list2[i] not in list1:
				new_list.append(list2[i])
			i+=1
	print(new_list)
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
(common_elements(list1,list2))
#Q.8 saral more exercises