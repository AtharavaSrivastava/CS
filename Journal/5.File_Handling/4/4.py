#Program to copy the content of a file to another file, skipping lines that contain the letter 'a'
#Creating the 1st text file and writing in it
f=open('text.txt','w')
l1='The quick brown fox jumps over the lazy dog\n'
l2='The five boxing wizards jump quickly\n'
l3='Six big devils from Japan quickly forgot how to waltz\n'
l4='This line is the fourth line\n'
l5='This line is the fifth line\n'
f.writelines([l1,l2,l3,l4,l5])
f.close()

#Checking the first file's lines for the letter 'a' and adding the required ones to file 2.
f=open('text.txt','r')
f2=open('text2.txt','w')

for line in f.readlines():
    if 'a' in line or 'A' in line:
        pass
    else:
        f2.write(line)
f.close()
f2.close()


#Displaying both the files
f=open('text.txt','r')
print('This is the first file:')
print(f.read())
print()
f2=open('text2.txt','r')
print('This is the second file:')
print(f2.read())
        
            
            
