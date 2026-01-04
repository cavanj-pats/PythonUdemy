#4
#  create a dictionary to keep track of how many times a user has logged in
# login userID's are presented in a list


users = ['John', 'Bob','Alex', 'Alice', 'John', 'Charlie', 'Alex', 'Alice','John','Alex']
logins = {}

for u in users:
    if u in logins:
        logins[u] += 1
    else:
        logins[u]=1


#print(logins)

# Abdul looped through the dictionary for printing
for user, count in logins.items():
    print(f"{user:8}: {count}" )
