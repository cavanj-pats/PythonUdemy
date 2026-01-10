#4
#  create a dictionary to keep track of how many times a user has logged in
# login userID's are presented in a list

original ={'a':1,'b':2,'c':1, 'd':2, 'e':3, 'f':2}

#swap keys for values
inverted = {}   #empty brackets won't create a set they'll create an empty dictionary

for k, v in original.items():
    if v not in inverted:
        inverted[v] = {k}

    else:
        inverted[v].add(k)
        

print ("Inverted Dictionary:" , inverted)

