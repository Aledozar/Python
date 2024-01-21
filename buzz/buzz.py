#Program that prints the integers from 1 to 100. 
#But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".

for _ in range(1,101):
    if (_ %3==0) and (_ %5==0):
        print( 'FizzBuzz')
    elif _ % 3 ==0:
        print('Fizz')
    elif _ % 5 ==0:
        print('Buzz')
    else:
        print(_)