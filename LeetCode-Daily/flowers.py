# https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/?envType=daily-question&envId=2023-10-11

# memory limit exceeds in this answer -_-

def fullBloomFlowers(flowers, people):
    """
    :type flowers: List[List[int]]
    :type people: List[int]
    :rtype: List[int]
    """
    garden = [0]*max(max(inner_list[1] for inner_list in flowers), max(item for item in people))
    ans = [0]*len(people)
    for i in range (0, len(flowers), 1):
        for j in range (flowers[i][0], flowers[i][1]+1, 1):
            garden[j-1] += 1
    for i in range (0, len(people), 1):
        ans[i] = garden[people[i]-1]
    return ans

print(fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]))
print(fullBloomFlowers([[19,37],[19,38],[19,35]], [6,7,21,1,13,37,5,37,46,43]))


#Time limit exceeds in this answer -_-
def fullBloomFlowers(flowers, people):
    """
    :type flowers: List[List[int]]
    :type people: List[int]
    :rtype: List[int]
    """
    #garden = [0]*max(max(inner_list[1] for inner_list in flowers), max(item for item in people))
    ans = [0]*len(people)
    for i in range(0, len(people), 1):
        for j in range (0, len(flowers), 1):
            if people[i]-1 >= flowers[j][0]-1 and people[i]-1 <= flowers[j][1]-1:
                ans[i]+=1
    return ans
    
print(fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]))
print(fullBloomFlowers([[19,37],[19,38],[19,35]], [6,7,21,1,13,37,5,37,46,43]))

#Time limit exceeds in this answer -_-
def fullBloomFlowers(flowers, people):
    """
    :type flowers: List[List[int]]
    :type people: List[int]
    :rtype: List[int]
    """
    start_bloom = [flower[0] for flower in flowers]
    end_bloom = [flower[1] for flower in flowers]
    ans = [0]*len(people)
    for i in range(0, len(people), 1):
        ans[i] = sum(1 for x in start_bloom if x <= people[i]) - sum(1 for x in end_bloom if x < people[i])
    return ans
    
print(fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]))
print(fullBloomFlowers([[19,37],[19,38],[19,35]], [6,7,21,1,13,37,5,37,46,43]))