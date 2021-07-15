def is_leap(year):
    leap = False
    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0):
        	leap = False
        	if (year % 400 == 0):
        		leap = True
    return leap
print(is_leap(2010))
#leap year in function
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
print(is_leap(2016))
#leap year in multiple 