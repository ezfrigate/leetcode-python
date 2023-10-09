#https://leetcode.com/problems/valid-anagram/

#Extendable to all ASCII values by replacing ord('a') by 0
class Solution(object):
    def isAnagram(self, s, t):
        # Create a list of 26 zeroes
        lst = [0] * 26
        if(len(s) != len(t)):
             return False
        # Each time a letter appears in s increase that letter's position by 1 and if it appears in t, reduce it by 1
        for char_s, char_t in zip(s, t):
                # Increment the count for the corresponding letter in s
                lst[ord(char_s) - ord('a')] += 1

                # Decrement the count for the corresponding letter in t
                lst[ord(char_t) - ord('a')] -= 1

        # Check if all elements in letter_counts are equal to 0
        return all(count == 0 for count in lst)
    
obj = Solution()
print(obj.isAnagram('aba', 'aba'))
print(obj.isAnagram('aba', 'abb'))
print(obj.isAnagram('aba', 'baa'))
print(obj.isAnagram('', ''))
print(obj.isAnagram('aba', ''))
print(obj.isAnagram('', 'aba'))

# Efficient if constraint on char is followed
class Solution(object):
    def isAnagram(self, s, t):
        if (len(s) != len(t)):
            return False
        X = 'abcdefghijklmnopqrstuvwxyz'
        for letter in X:       
            if s.count(letter) != t.count(letter):
                return False
        return True
    
obj = Solution()
print(obj.isAnagram('aba', 'aba'))
print(obj.isAnagram('aba', 'abb'))
print(obj.isAnagram('aba', 'baa'))
print(obj.isAnagram('', ''))
print(obj.isAnagram('aba', ''))
print(obj.isAnagram('', 'aba'))