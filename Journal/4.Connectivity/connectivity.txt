#Importing required library
import mysql.connector as sq

#Creating database and table
mydb = sq.connect(host="localhost",user="root",password="root")
mycur = mydb.cursor()
mycur.execute("Create database Company")
mycur.execute("Use Company")
mydb.commit()
mycur.execute("Create table Employee (Emp_ID int, Emp_name varchar(50), Salary int)")
mydb.commit()
   
#Inserting the data into the table
id_=[114,115,116,117,118]
name=['Jhon','Jane','Matt','Woods','Sam']
salary=[111111,222222,333333,444444,555555]
for i in range(5):
    sql='insert into employee values (%s,%s,%s)'
    mycur.execute(sql,(id_[i],name[i],salary[i]))

#Displaying all the data
mycur.execute('select*from employee')
print('This is all the data:')
print(mycur.fetchall())
print()


#Displaying the row count
print('The number of rows in the table are:',mycur.rowcount )
print()


#Updating the salary of an employee
mycur.execute('update employee set salary=60000 where emp_id = 116')


#Displaying the first row of the table only
mycur.execute('select*from employee')
print('This is the first row of the table:',mycur.fetchone())
