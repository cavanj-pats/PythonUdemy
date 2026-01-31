#valid work age and exception handling

#challenge

#create a class that inherits from Exception class
#once we learn more we can perhaps add more functionalit to this class
#for now, we only need to enter 'pass'
class InvalidAgeError(Exception):
    pass


def validate_age(age):
    if age >= 18 and age <=60:
        return True
    else:
        raise InvalidAgeError('Age should be between 18-60')


name = input('Enter Name:')
age = int(input('Enter Age:'))

try:
    validate_age(age)
    print('You can join Work')
except InvalidAgeError as e:
    print(e)