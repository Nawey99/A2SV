# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        for char in count.keys():
            count[char] -= 1
            unique_counts = set(_count for _count in count.values() if _count)
            if len(unique_counts) == 1:
                return True
            count[char] += 1
        return False

        
