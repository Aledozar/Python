#MAKES TWENTY: 
#Given two integers, return True if the sum of the integers is 20 
#or if one of the integers is 20. 
#If not, return False

def makes_twenty(n1,n2):
    if n1+n2==20:
        return True
    elif n1==20:
        return True
    elif n2==20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))