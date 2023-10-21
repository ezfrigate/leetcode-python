#https://leetcode.com/problems/can-place-flowers/
def canPlaceFlowers(flowerbed, n):
    for i in range(0, len(flowerbed)):
        if flowerbed[i] == 0:
            if (flowerbed[i-1] == 0 or i == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n-=1
    return n<=0

print(canPlaceFlowers([1,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,1], 1))

print(canPlaceFlowers([0,0,1,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1,0,0], 1))