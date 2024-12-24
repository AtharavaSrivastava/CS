#Function to check if the number is an armstrong number or not and to display it accordingly
def armstrong(num):
    #Initializing sum
    summ = 0
    temp = num

    #Finding the sum of the cube of each digit
    while temp > 0:
       digit = temp % 10
       summ += digit ** 3
       temp //= 10

    #Printing the result
    if num == summ:
       print(f'{num} is an Armstrong number')
    else:
       print(f'{num} is not an Armstrong number')

#Accepting number from the user and executing the function 
num = int(input("Please enter a number: "))
armstrong(num)
