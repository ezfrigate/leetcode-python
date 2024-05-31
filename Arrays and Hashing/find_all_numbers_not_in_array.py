#Beats Memory

def findDisappearedNumbers(nums):
    for i in range (0, len(nums), 1):
        nums[(nums[i] - 1)%len(nums)] = nums[(nums[i]-1)%len(nums)] + len(nums)
    ans = []
    for i in range (0, len(nums), 1):
        if(nums[i] <= len(nums)):
            ans.append(i + 1)
    return ans
 
print(findDisappearedNumbers([1,1]))
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))

#Beats Time

def findDisappearedNumbers(nums):
    return set(range(1, len(nums)+1)) - set(nums)

print(findDisappearedNumbers([1,1]))
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))