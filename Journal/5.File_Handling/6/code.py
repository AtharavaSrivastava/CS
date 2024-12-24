#Program to write and read a csv file.
import csv

#Creating the csv file and writing in it.
f=open('file.csv','w') 
writer=csv.writer(f)
records=[['Name','ID'],['Jhon',1],['Jane',2],['Matt',3],['Woods',4],['Sam',5]]
writer.writerows(records)
f.close()

#Reading the file.
f=open('file.csv','r',newline='\r\n')
reader=csv.reader(f)
for record in reader:
    print(record)
f.close()
