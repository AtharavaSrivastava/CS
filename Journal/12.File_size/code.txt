#Display file size after removing EOL characters, leading and trailing whitespaces, and blank lines

file=input('Please enter the file name: ')

try :
    with open (file,'r') as file:
        cleaned_lines=[line.strip() for line in file.readlines() if line.strip()]
        cleaned_content = " ".join(cleaned_lines)
        print("Size of file after cleaning:", len(cleaned_content), "bytes")       
except FileNotFoundError:
    print("File not found.")
    
