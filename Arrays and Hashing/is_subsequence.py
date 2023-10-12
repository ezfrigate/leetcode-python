#https://leetcode.com/problems/is-subsequence/

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) == 0: return True
    if len(s) > len(t): return False
    j = 0
    for i in range (len(t)):
        if(t[i] == s[j]):
            j+=1
            if j==len(s):
                return True
        i+=1
    return False

print(isSubsequence('ace', 'abcdefghijklmnop'))
print(isSubsequence('', 'abcdefghijklmnop'))
print(isSubsequence('ace', ''))
print(isSubsequence('b', 'b'))
print(isSubsequence('b', 'c'))
print(isSubsequence('axc', 'ahbgdc'))