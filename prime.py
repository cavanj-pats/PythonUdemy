#prime.py


def printFactors(number):
    for x in range(1, number):
        if number % x == 0:
            print (x)
        if x > number/2:
            break


    print (number)


def isPrime(number):
    count = 0
    for x in range(1, number+1):
        if number % x == 0:
            count += 1
        if x > number/2:
            break
    
    if count == 2:
        return True
    else:
        return False
    


number = int(input("Enter the number to check divisors: "))

printFactors(number)
print(isPrime(number))

for i in range(1, 101):
    if (isPrime(i)):
        print (i, ',')