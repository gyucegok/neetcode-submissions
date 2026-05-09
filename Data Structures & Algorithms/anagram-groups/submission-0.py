class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        my_dict = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))
            my_dict[sorted_word].append(word)
        
        return [my_dict[x] for x in my_dict]
            

