#Program to search for a student by name in the binary file.
#Importing required library
import pickle

#Creating the search function
def search(name):
    f=open('C://Users//sriva//Desktop//School//Journal//5. File_Handling//2//Student.bin','rb')
    while True:
        try:
            name1,roll_no=pickle.load(f)
            if name1==name:
                return roll_no,name
        except EOFError:
            break
    return none

#Searching for the name 'Jhon'
print(search('Jhon'))
