#backtracking_findSubsets.py

#find all subsets

nums = [1,2,3]
ans, sol = [], []
i = 0
def backtrack(i):

    
        #there are two options.   exclude or include
    if i == len(nums):
        ans.append(sol[:])
        #ans.append([]) # the algorithm will not return a null list but it is a valid subst
        return
    else:
        #include result
        #ans.append(sol[:])
        sol.append(nums[i]) #include 1 in solution
        backtrack(i+1)
        sol.pop() #exclude i in solution
        backtrack(i+1)
    


        



backtrack(0)
print(ans)