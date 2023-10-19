# https://leetcode.com/problems/remove-element/description/
def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i]==val:
            nums[i], nums[-count-1] = nums[-count-1], nums[i]
            nums[-count-1] = '_'
            count+=1
    return nums

print(removeElement([0,1,2,2,3,0,4,2], 2))