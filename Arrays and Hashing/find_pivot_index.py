def pivotIndex(nums):
    rsum = 0
    lsum = 0
    l = 0
    r = len(nums) - 1
    while(r - l > 2):
        if(rsum > lsum):
            lsum = lsum + nums[l]
            l=l+1
        else:
            rsum = rsum + nums[r]
            r=r-1
    return (r+l)//2

print(pivotIndex([1,7,3,6,5,6]))

def pivotIndex(nums):
    rsum = sum(nums)
    lsum = 0
    for i in range(len(nums)):
        rsum = rsum - nums[i]
        if i != 0 :
            lsum = lsum + nums[i-1]
        if lsum==rsum: return i
    return -1

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex([2,1,-1]))
print(pivotIndex([1,2,3]))
print(pivotIndex([-1,-1,0,1,1,0]))