que_list = [".How many continents are there?",".What is the capital of India?",       ".NG mei kaun se course padhaya jaata hai?","What is Hackathon?"]
opt_list= [["Four", "Nine", "Seven", " Eight"],[" Chandigarh", "Bhopal", " Chennai", "Delhi"],["Software Engineering", " Counseling", "Tourism", "Agriculture"],["One who hacks","It is a place in Jharkhand","An event in which a large number of people meet to engage in collaborative computer programming.","It is nothing but task"]]
ans_list=[3,4,1,3]
fifty_list=[['four','seven'],['Delhi','Bhopal'],['Tourism','software engineering'],["It is a place in Jharkhand","An event in which a large number of people meet to engage in collaborative computer programming."]]
sol_list=[3,4,1,3]  
lifelinecount = 0
def lifeline(index):  
    global lifelinecount
    j=0 
    if(lifelinecount==0): 
        while j<len(fifty_list[index]):
            print(j+1,fifty_list[index][j])
            j=j+1
        user_ans = int(input('enter the option'))
        lifelinecount+=1
        if user_ans==sol_list[index]:
            return True
        else:
            return False
    else:
        print('you Already used 5050')
        return "no"    
def option(index):
    j=0
    while j<len(opt_list[index]):
        print(j+1,opt_list[index][j])
        j=j+1
    user_ans = int(input('enter the option'))
    if user_ans==ans_list[index]:
        return True
    if user_ans == 5050:
        return(lifeline(index))
    else:
        return False

def que():
    print("  Co-powered by Dabur Amla and sponsered by Patanjali Kaun Banega Crorepati mein apka Swagat hai,shadab aadab shastriyakaal!")
    index=0
    Rupees=100000
    while index<len(que_list):
        
        print("Q.",index+1,que_list[index],)
        result=option(index)
        if result == "no":
            index-=1
        elif result==True:
            print("Congrats,ap jit gye",Rupees)
            if Rupees==400000:
            	print("you are winner Apne jeeta hai dabur Amla aur patanjali ke taraf se ek gift hamper !")
        else:
            print( "bahut hi dukh hua,ap har gaye !")
            print("shubhratri,shabbakhair Jaate Jaate Do baat,2 gaj duri mask jaruri,dhyan rakhiye and wear mask!")
            break 
        index+=1
        Rupees+=200000

def main():
    que()
main()