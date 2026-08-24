class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        maxm = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            maxm = max(maxm, curr)

        return maxm / k
        