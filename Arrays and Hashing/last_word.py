def lengthOfLastWord(s):
    if(len(s) == 1 and s != ' '): return 1
    i = 0
    while s[len(s)-i-1] == ' ':
        i += 1
    if i == len(s)-1 : return i
    j = 0
    while s[len(s)-i-1] != ' ':
        i += 1
        j += 1
    return j

print(lengthOfLastWord('word'))
print(lengthOfLastWord(' word '))
print(lengthOfLastWord(' word'))
print(lengthOfLastWord('word '))
print(lengthOfLastWord('a'))
print(lengthOfLastWord(' a'))
print(lengthOfLastWord('a '))