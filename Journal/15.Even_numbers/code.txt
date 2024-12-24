#Adding even numbers to list

num=input('Please enter the numbers separated by space: ')

def even_numbers(numbers):
    global num
    l=num.split(' ')
    even_numbers=[]
    for i in l:
        if int(i)%2==0:
            even_numbers.append(int(i))

    print(f'List of even numbers: {even_numbers}')

even_numbers(num)     
