class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a= []
        nums.sort()
        b , c = 0 , 0
        for i in range(0,len(nums)):
            a.append(i+1)
        
        for i in range(0,len(nums)):
            if nums[i]== nums[i-1]:
                c = nums[i]

            if a[i] not in nums :
                b = a[i]   
        return [c,b]
