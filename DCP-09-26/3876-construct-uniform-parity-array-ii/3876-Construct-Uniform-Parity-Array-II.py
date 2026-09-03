class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = float('inf')
        oddCnt = 0
        for x in nums1 :
            mn = min(mn, x)
            if x % 2 == 1:
                oddCnt += 1
        return mn % 2 == 1 or oddCnt == 0