#Function to check if the number is perfect or not and diplaying the output accordingly
def perfect(num):
    summ=0
    for i in range(1,num):
        if num%i==0:
            summ+=i
    if summ==num:
        print(f'{num} is a perfect number.')
    else:
        print(f'{num} is not a perfect number.')

#Accepting the number from the user and executing the function
num=int(input('Please enter the number you want to check:'))
perfect(num)
