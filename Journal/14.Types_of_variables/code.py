#Demonstrate the usage of local and global variables

var=153

def function():
    global var
    print(f'Updated value of global variable var={var+100}')
    char=142
    print(f'Value of local variable char={char}')

function()
print(f'Original value of global variable var={var}')
