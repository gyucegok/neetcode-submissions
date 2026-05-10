class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        maximum_area = 0

        while left < right:
            width = right - left
            height = min(heights[right], heights[left])
            area = width * height

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

            maximum_area = max(area, maximum_area)
        
        return maximum_area
            
        