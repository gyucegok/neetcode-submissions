class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 substring, s2 full-string

        if len(s2) < len(s1):
            return False

        from collections import Counter
        s1_count = Counter(s1)

        for i in range(len(s2)):
            s2_slice = s2[i:i+len(s1)]
            if Counter(s2_slice) == s1_count:
                return True
        return False
        