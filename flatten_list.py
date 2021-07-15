def nested(GivenList):
        for i in GivenList:
            if type(i) == list:
            	nested(i)
            else:
            	new_list.append(i)
new_list = []
GivenList = [1,2,3,[4,[5,6,[7]],8],[9]]
nested(GivenList)
print (GivenList)
print (new_list)