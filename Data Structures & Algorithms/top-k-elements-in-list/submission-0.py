class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        my_dict = Counter(nums)
        return [x[0] for x in my_dict.most_common(k)]
        