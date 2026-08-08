#backtracking_findSubsets.py

#find all subsets

nums = [1,2,3]
ans, sol = [], []

def backtrack():


    if sol == nums:
        #ans.append(sol[:]) #this is a deep copy not a reference copy
        return
    for i in nums:
        ans.append(sol[:])
        sol=i
        backtrack


print(ans)