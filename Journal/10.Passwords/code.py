#Program to create a CSV file by entering user-id and password, read and search the password for given userid.
import csv
#Function to create csv file
def create():
    with open ('file.csv','w') as f:
        writer=csv.writer(f)
        data=[['user_id','Password'],['Jhon','Accipiters!00'],['Jane','Charlie*23'],['Matt','Luna@863'],['Woods','Syphus!007'],['Sam','Welson!23']]
        writer.writerows(data)

#Function to read the csv file and search for the user_id and display the password.
def find(user_id):
    data=[]
    with open ('file.csv','r',newline='\r\n') as f:
        reader=csv.reader(f)
        for record in reader:
            data.append(record)        
        for i in range (1,len(data)):
            if user_id==data[i][0]:
                print(f'The password for the user id {user_id} is {data[i][1]}')
                break
            elif user_id!=data[i][0]:
                print('Not found')
                break

#Accepting the user_id which has to be searched
user_id=input('Please enter the user id you want to search for :')

#Executing the functions
create()
find(user_id)
