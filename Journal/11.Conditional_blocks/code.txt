#Program to demonstrate usage of try, execpt and finally blocks

try :
    num1=int(input('Please enter the dividend: '))
    num2=int(input('Please enter the divisor: '))
    print(f'The quotient when {num1} is divided by {num2} is {num1/num2}')
except ZeroDivisionError:
    print('Division by 0 is not possible')
except ValueError:
    print('Please enter a valid number.')
finally:
    print('Execution complete.')
