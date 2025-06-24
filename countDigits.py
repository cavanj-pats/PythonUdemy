#count digits


n = 1771
r = 0
i = 0   #counter
rev = 0   #for reversing a number
sum = 0
m = n

while n>0:
    r =  n % 10
    sum = sum + r
    n = n // 10
    i = i + 1
    rev = rev*10 + r

print (i, 'Count of digits')
print (sum, 'Sum of Digits')
print (rev, 'Number reversed')
if rev == m:
    print(rev, 'is Palindrome of ', m)
else:
    print(rev, ' is NOT a Pali of ', m)