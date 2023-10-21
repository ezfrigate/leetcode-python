#https://leetcode.com/problems/isomorphic-strings/
def isIsomorphic(s, t):
    dict = {}
    if(len(s) == len(t)):
        for i in range(0, len(s), 1):
            if(dict.get(s[i]) == None and t[i] not in dict.values()):
                dict[s[i]] = t[i]
            elif(dict.get(s[i]) != t[i]):
                return False
    else: return False
    return True

print(isIsomorphic("egf", "add"))
print(isIsomorphic("egg", "add"))
print(isIsomorphic("egg", "ade"))