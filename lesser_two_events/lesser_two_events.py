#lesser of two evens
def lesser_of_two_evens(a,b):
    
    if a%2 == 0 and b%2 ==0:
        if a > b:
            return b
        elif b>a:
            return a
        pass
    elif a%3 ==0 or b%2==0:
        if a > b:
            return a
        elif b>a:
            return b
        pass
    elif a%2==0 or b%3==0:
        if a > b:
            return a
        elif b>a:
            return b
        pass
