class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n = len(nums)

        min_val = [0] * n
        min_val[n - 1] = nums[n - 1]

        for i in range(1, n):
            min_val[n - i - 1] = min(
                nums[n - i - 1],
                min_val[n - i]
            )

        max_val = nums[0]

        for i in range(n):
            max_val = max(nums[i], max_val)

            diff = max_val - min_val[i]

            if diff <= k:
                return i

        return -1