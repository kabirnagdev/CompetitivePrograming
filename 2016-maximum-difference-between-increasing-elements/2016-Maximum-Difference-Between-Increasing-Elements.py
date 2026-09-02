class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minval = nums[0]
        maxd = -1
        for i in range(0, len(nums)):
            if nums[i] < minval  :
                minval  = nums[i]
            if nums[i]> minval :
                if nums[i]-minval > maxd :
                    maxd = nums[i]-minval
                
        return maxd

        