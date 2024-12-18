#Program to read a text file and display the number of vowels,consonant,uppercase,lowercase and characters in the file

#Opening the file and converting it into a string
f=open('C://Users//sriva//Desktop//School//Journal//5. File_Handling//5//text.txt','r')
lines=f.readlines()
string=''.join(lines)

#Counting the number of characters
char=0
for ch in string:
    char+=1
    
#Counting the vowels and the consonants
vowels = ['a','e','i','o','u','A','E','I','O','U']
vowels_count=0
consonants_count=0

for i in string:
    if i in vowels :
        vowels_count +=1
    elif i !=' ' :
        consonants_count+=1

#Counting the uppercase and lowercase characters
Uppercase_count = 0
Lowercase_count = 0
new_string = ''

for i in string :
    if (i.isupper()) == 1:
        Uppercase_count+=1
        new_string+=(i.lower())
    elif (i.islower()) == 1:
        Lowercase_count+=1
        new_string+=(i.upper())


#Displaying the required output
print(f'There are {char} characters in the file.')
print(f'There are {vowels_count} vowels in the file.')
print(f'There are {consonants_count} consonants in the file.')
print(f'There are {Uppercase_count} uppercase characters in the file.')
print(f'There are {Lowercase_count} lowercase characters in the file.')
