try:
    num1 = int(input('Enter a number:'))
    num2 = int(input('Enter another number:'))

    results = num1/num2
    print(results)

except Zerodivisionerror:
    print('Error, divisions by zero is not allowed')

except valueerror:
    print('Please enter a valid number')

except exception as e:
    print(e)

else:
    print('No exceptions were raised')

finally:
    print('Execution completed')
