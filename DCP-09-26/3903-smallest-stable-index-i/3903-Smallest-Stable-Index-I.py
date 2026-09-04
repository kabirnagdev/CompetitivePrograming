class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ins = -1
        a = [ ]
        for i in range (0,len(nums)):
            if i <1 : 
                curr = nums[0] - min(nums[i:len(nums)])
            else: 
                curr = max(nums[0:i]) - min(nums[i:len(nums)])
            a.append(curr)
            if curr <=k :
                return i 
        return -1
  
        
        