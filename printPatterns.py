# print * patterns


for i in range (1, 6):
    for j in range (1, 6):
        print('*', end=' ')
    print('')

print ('')


#method 2 fro printing lower diag matrix
for i in range(1, 6):
    for j in range(0, i):
        print('*', end=' ')
    print('')

print('')
#method 3 for printing patter. Lower diag matrix
for i in range(1, 6):
    print('* ' * i)


print('')

#left upper diag matrix of *
for i in range(1, 6):
    for j in range(1, 6 - (i-1)):
        print('*', end=' ')
    print('')

print('')
#left upper
for i in range(1, 6):
    print('* ' * (6-i))

#right upper
print("right upper matrix of *")
for i in range(1, 6):
    print('  '* (i-1), end=' ') # need to print two space
    print('* '* (5-(i-1)))