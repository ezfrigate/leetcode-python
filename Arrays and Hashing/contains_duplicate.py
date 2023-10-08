#https://leetcode.com/problems/contains-duplicate/

#Beats time, uses set
class Solution:
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)
    
obj = Solution()
print(obj.containsDuplicate([1,2,3,4,5]))
print(obj.containsDuplicate([1,2,3,4,4]))
print(obj.containsDuplicate([]))

#Using lambda
class Solution:
    containsDuplicate = lambda self, nums: len(set(nums)) != len(nums)

obj = Solution()
print(obj.containsDuplicate([1,2,3,4,5]))
print(obj.containsDuplicate([1,2,3,4,4]))
print(obj.containsDuplicate([]))

#Beats memory, uses loop
class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        i = 0
        while(i < len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            i+=1
        return False
    
obj = Solution()
print(obj.containsDuplicate([1,2,3,4,5]))
print(obj.containsDuplicate([1,2,3,4,4]))
print(obj.containsDuplicate([]))