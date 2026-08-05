# permutations leet   Greg Hogg You Tube


nums = [1,2,3]

ans, sol = [], []

def backtrack():

    if len(sol) ==  len(nums):
       ans.append(sol[:])
       return

    for i in nums:
        if i not in sol:
            sol.append(i)
            backtrack()
            sol.pop()

    return ans

backtrack()
print(ans)
