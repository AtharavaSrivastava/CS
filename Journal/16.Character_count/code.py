#Calculate uppercase and lowercase characters in a string

def counting(string):
    l=string.split(' ')
    uppercase_count=0
    lowercase_count=0
    for i in l:
        for j in i:
            if j.isupper():
                uppercase_count+=1
            elif j.islower():
                lowercase_count+=1

    print(f'Number of uppercase characters is: {uppercase_count}')
    print(f'Number of lowercase characters is: {lowercase_count}')

char=input('Please enter the string: ')
counting(char)
