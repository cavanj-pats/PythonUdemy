#String and related methods
#project files and exercises for practice

#credit card processing.  Take in 16 digit string and mask first 12 digits
#printing only X placeholders and the last four digits
#  7451-6789-9876-5432 should print as XXXX-XXXX-XXXX-5432

'''
str = input('Enter 16 digit credit card number, include the dashes: ')
#this is the way abdul did it. i simply did 'XXXX-XXXX-XXXX-'
four = 'X' *4 + '-'
str2 = four * 3 + str[15:]
print (str2)

'''


'''
#URL Parsing
str = input('Enter a URL for parsing: ')
pPos = str.find('://')
d1Pos = str.find('.')
d2Pos = str.find('.', d1Pos+1)
pagePos = str.find('/', d2Pos+1)

protocol = str[:pPos]
domain = str[d1Pos+1:d2Pos]
page = str[pagePos:]

print ('Protocol: ' + protocol)
print ('Domain: ' + domain)
print ('Page: ' + page)

'''

'''
#palindrome project   'Race car',  'Poop', etc.
str1 = input('Enter a string for Pali-testing: ')
strP1 = (str1.lower()).replace(' ','')
strP2 = strP1[::-1]

if (strP1 == strP2):
    print ('Is Palindrome: ' + strP1)
else:
    print ('Is Not Pali, so make it Pali: ' + strP1 + strP2)

'''
'''

#anagrams   Project.   A little tougher
str1 = 'Snooze Alarms'
str2 = "Alas, no more Z's"
str1 = str1.lower()
str2 = str2.lower()

for x in str1:
    if x.isalpha():
        if str1.count(x) != str2.count(x):
            #is not an anagram
            print('Is Not Anagram')
            break
else:
    print('Is Anagram!')

'''


'''
#data cleaning a scanned text string
strScan = 'Data/needs<to@be^cleaned'
strClean = ''

for x in strScan:
    if x.isalpha() or x.isspace():
        strClean = strClean + x
    else:
         strClean = strClean + ' '
        
    
print (strClean)
'''


#password change project
newPassword = 'Nice.Pooper1'
confirmPassword = 'Nice.PoopeR1'

if newPassword == confirmPassword:
    print ('Password Change successful')
else:
    if newPassword.casefold() == confirmPassword.casefold():
        print('Check case and try again!')
    elif len(newPassword) != len(confirmPassword):
         print('Passwords different lengths!')
    else:
        print ('Passwords do not match!')