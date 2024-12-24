#Program to create a binary file and store student names with their roll numbers.
#Importing required library
import pickle

#Creating the file and writing in it
f=open('Student.bin','wb')
name=['Jhon','Jane','Matt','Woods','Sam']
roll_no=[1,2,3,4,5]
for i in range (5):
    pickle.dump((name[i],roll_no[i]),f)
f.close()



