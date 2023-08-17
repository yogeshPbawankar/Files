class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # importing the counter module from collections
        from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # counter is used to count no of occurance.
        magazine_count = Counter(magazine)
        ransomNote_count = Counter(ransomNote)
        
        #it checks if the charecter eixt or less than count.
        for char, count in ransomNote_count.items():
            if char not in magazine_count or magazine_count[char] < count:
                return False
        
        return True

        solution = Solution()

# Test Case 1: Positive case
ransomNote1 = "aa"
magazine1 = "aab"
