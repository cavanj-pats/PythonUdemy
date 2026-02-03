#journal program
#journal.txt

import os

def clear_console():
    # Detect the operating system
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for macOS and Linux (posix)
        _ = os.system('clear')

def jwrite(entry):
    try:
        file = open('journal.txt', 'a')
    except Exception as e:
        print(e)
    else:
        file.write(entry + '\n')
   
        file.close()

def jread():
    try:
        file = open('journal.txt', 'r')
    except Exception as e:
        print(e)
    else:
        data = file.readlines()
        file.close()
        clear_console()
        print("Journal Entries:\n")
        for d in data:
            print(d)
            #print("\n")


def jsearch(search_text):
    idx = 0
    try:
        file = open('journal.txt', 'r')
    except Exception as e:
        print(e)
    else:
        data = file.readlines()
        file.close()
        print ('\n')
        for d in data:
            idx = d.find(search_text)
            if (idx != -1):
                return ('Journal Entry Found! ' + d)   # return the entry with the found text
    
        return  "Not Found! " + search_text    
        


clear_console()

loop = True

while loop:
    
    print("Journal Manager -- Activity Menu\n")
    print("1. Write Journal Entry")
    print("2. Read Journal")
    print("3. Search for Journal Entry")
    print("4. Exit Journal Manager\n")
    
    
    selection = int(input("Please enter menu selection: "))

    if (selection == 1):
        #open for writing / appending
        entry = input("Enter Text to write to journal: ")
        jwrite(entry)

    elif(selection == 2):
        jread()
    elif(selection == 3):
        #
        print (jsearch(input("\nEnter Text to search: ")))
        print ('\n')
    elif(selection == 4):
        #    
        loop = False
    else:
        clear_console()
        print("\nPlease enter a valid selection.\n")
        