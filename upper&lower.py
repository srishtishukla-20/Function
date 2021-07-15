def count(s):
    lower=0
    upper=0
    i=0
    while i<len(s):
        if s[i].isupper():
            upper+=1
        elif s[i].islower():
            lower+=1
        else:
           pass
        i+=1
    print ("No. of Upper case characters : ", upper)
    print ("No. of Lower case Characters : ", lower)
s="The quick Brown Fox"
count('The quick Brown Fox')