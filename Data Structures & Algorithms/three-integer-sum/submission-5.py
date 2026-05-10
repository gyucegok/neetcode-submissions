class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        my_list = []
        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue 

            left, right = i+1 , len(nums) - 1
            while left < right:
                complement = nums[i] + nums[left] + nums[right]
                if complement == 0:
                    my_list.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1 

                elif complement > 0:
                    right -= 1
                else:
                    left += 1
        return my_list


        