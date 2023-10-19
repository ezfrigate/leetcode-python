# https://leetcode.com/problems/pascals-triangle/submissions/

def generate(numRows):
    lst = [ [1] for _ in range(numRows) ]
    for i in range(1, numRows, 1):
        for j in range(1, numRows, 1):
            if j<i :
                lst[i].append(lst[i-1][j] + lst[i-1][j-1])
            elif j==i:
                lst[i].append(1)
    return lst

print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(5))