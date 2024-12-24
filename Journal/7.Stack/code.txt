#Stack program
a=0
stk=[]
top=0

def isempty(stk):
    if stk==[]:
        return True
    else :
        return False
def push(stk,data):
    global top
    stk.append(data)
    top=len(stk)-1
    print(f'{data} has been added to the stack')

def pop(stk):
    global top
    if isempty(stk):
        print('The stack is empty!')
    else:
        i=stk.pop()
        if len(stk)==0:
            top=0
        else:
            print(f'The is the popped item: {i}')
            top-=1

def peek(stk):
    if isempty(stk):
        print('The stack is empty!')
    else :
        print(f'This is the top-most item: {stk[len(stk)-1]}')
def show(stk):
    if isempty(stk):
        print('The stack is empty!')
    else:
        print(f'{stk[len(stk)-1]} <----Top')
        for i in range (len(stk)-1):
            print(stk[i])



while a==0:
    print('Menu')
    print('1.Push')
    print('2.Pop')
    print('3.Peek')
    print('4.Show')
    print('5.Exit')
    choice = int(input('Please enter your choice of menu item:'))
    print()
    if choice==1:
        data=input('Please enter the data you want to add to the stack:')
        push(stk,data)
        print()
    elif choice==2:
        pop(stk)
        print()
    elif choice==3:
        peek(stk)
        print()
    elif choice==4:
        show(stk)
        print()
    elif choice==5:
        print('Thank You!\nHope you have a nice day!')
        a=1
    else:
        print('Invalid input')
        
    
