class Solution(object):
    def twoSum(self, nums, target):
        for item in nums :
            if target-item in nums and item != target/2:
                return [nums.index(item), nums.index(target-item)]
        return [i for i, x in enumerate(nums) if x == target/2]
            
obj = Solution()
print(obj.twoSum([2, 3, 4, 6], 7))
print(obj.twoSum([3, 3], 6))
print(obj.twoSum([1, 3, 3], 6))

#Not my solution, I thought will consume more time.
class Solution(object):
    def twoSum(self, nums, target):
        numToIndexMap = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndexMap:
                return [numToIndexMap[target - nums[i]], i]
            numToIndexMap[nums[i]] = i
        return []

obj = Solution()
print(obj.twoSum([2, 3, 4, 6], 7))
print(obj.twoSum([3, 3], 6))
print(obj.twoSum([1, 3, 3], 6))