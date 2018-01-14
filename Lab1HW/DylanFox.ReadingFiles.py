#Dylan Fox
#Reading Files

def main():
    file = open(input("File Name: "))
    text = file.readlines()
    lineNumber = 1

    for line in text:
        print(lineNumber, line)
        lineNumber +=1

    file.close

main()
    
