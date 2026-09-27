class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        
        for i in range (len(nums)):
            counter = 1
            for j in range (i+1, len(nums)):
                if nums[i] == nums[j]:
                    j = j + 1
                    counter += 1
            if counter > len(nums) // 2:
                return nums[i]