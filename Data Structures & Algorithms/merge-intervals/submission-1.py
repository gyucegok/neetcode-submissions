class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        result = []

        intervals.sort(key=lambda x: x[1])

        while intervals:
            curr = intervals.pop()
            if intervals and curr[0] > intervals[-1][1]:
                result.append(curr)
            elif intervals and curr[0] <= intervals[-1][1]:
                intervals[-1] = [min(curr[0], intervals[-1][0]), max(curr[1], intervals[-1][1])]
            else:
                result.append(curr)
        return result

        







        