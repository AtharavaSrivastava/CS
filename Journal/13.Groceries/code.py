#Create and store information in 'Groceries' CSV file

import csv

no_of_items=int(input('Please enter the number of items you want to add: '))
print()
data=[]
for i in range (no_of_items):
    item_code=input('Please enter the item code: ')
    name=input('Please enter the item name: ')
    price=input('Please enter the price of item : ')
    quantity=input('Please enter the item quantity: ')
    print('----------------')
    data.append([item_code,name,price,quantity])

with open ('Groceries.csv','w',newline='') as f:
    writer=csv.writer(f)
    headers=['Item code','Name','Price','Quantity']
    writer.writerow(headers)
    writer.writerows(data)

print('Your data has been added to the file Groceries.csv')
