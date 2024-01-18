#BLACKJACK: Given three integers between 1 and 11, 
#if their sum is less than or equal to 21, return their sum. 
#If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
#if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    1 <= a,b,c <= 11
    
    if a+b+c <=21:
        return a+b+c
    elif a+b+c>21 and (a==11 or b==11 or c==11):
        return a+b+c-10
    else:
         return "BUST"
        
# Check
print(blackjack(5,6,7))
# Check
print(blackjack(9,9,9))
print(blackjack(9,9,11))