#https://leetcode.com/problems/length-of-last-word/description/

def lengthOfLastWord(s):
    ans = 0
    l = len(s)-1
    flag = False
    while(not (flag and s[l] == " ") and l >= 0):
        if(s[l] != " " and not flag):
            flag = True
        if(flag):
            ans = ans + 1
        l=l-1
    return ans

print(lengthOfLastWord('word'))
print(lengthOfLastWord(' word '))
print(lengthOfLastWord(' word'))
print(lengthOfLastWord('word '))
print(lengthOfLastWord('a'))
print(lengthOfLastWord(' a'))
print(lengthOfLastWord('a '))