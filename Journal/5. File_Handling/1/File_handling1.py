#Program to read a text file line by line and display each word separated by #

#Creating the text file and writing in it
f=open('text.txt','w')
l1='The quick brown fox jumps over the lazy dog\n'
l2='The five boxing wizards jump quickly\n'
l3='Six big devils from Japan quickly forgot how to waltz\n'
f.writelines([l1,l2,l3])
f.close()

#Displaying all the words separated by a '#'
f=open('text.txt','r')

for line in f.readlines():
    words="#".join(line.split())
    print(words)

