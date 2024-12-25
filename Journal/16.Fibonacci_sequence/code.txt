#Fibonacci seqeunce
num=int(input('Please enter the number of numbers you want of the Fibonacci sequnece: '))

def fibonacci_sequence(n):    
    num1=0
    num2=1
    next_number=num2  
    count=1
    while count <= n:
        print(next_number, end=" ")
        count+=1
        num1,num2=num2,next_number
        next_number=num1+num2
    print()

fibonacci_sequence(num)
