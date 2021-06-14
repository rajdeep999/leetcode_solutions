class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = s.strip().split(" ")
        return len(li[-1])
        
        