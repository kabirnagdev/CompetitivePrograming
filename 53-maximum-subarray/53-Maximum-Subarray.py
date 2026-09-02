class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs =  nums[0]
        currs = nums[0] 
        for i in nums[1:] :
            currs = max(i , currs+ i)
            maxs = max(maxs,currs)
        return maxs

        