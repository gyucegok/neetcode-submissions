class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = [] # Pair [temp,index]

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                sTemp,sIndex = stack.pop()
                result[sIndex] = i-sIndex
            stack.append([t,i])
        return result

            


        