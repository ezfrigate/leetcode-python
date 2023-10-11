#Clean ver:
class Solution(object):
    def replaceElements(self, arr):
        greatest = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], greatest = greatest, max(greatest, arr[i])
        return arr

obj = Solution()
print(obj.replaceElements([1,2,3,4,5,6,5,4,3,2,1]))
print(obj.replaceElements([400]))

class Solution(object):
    def replaceElements(self, arr):
        l = len(arr)
        greatest = -1
        i = len(arr) - 1
        while i > -1:
            l = arr[i]
            arr[i] = greatest
            if l > greatest:
                greatest = l
            i-=1
        return arr

obj = Solution()
print(obj.replaceElements([1,2,3,4,5,6,5,4,3,2,1]))
print(obj.replaceElements([400]))