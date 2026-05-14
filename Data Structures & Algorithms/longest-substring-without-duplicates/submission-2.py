class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_sub = 0
        for right in range(len(s)):
            if len(s[left:right+1]) == len(set(s[left:right+1])):
                max_sub = max(max_sub, len(s[left:right+1]))
            else:
                left +=1

        return max_sub


        
        