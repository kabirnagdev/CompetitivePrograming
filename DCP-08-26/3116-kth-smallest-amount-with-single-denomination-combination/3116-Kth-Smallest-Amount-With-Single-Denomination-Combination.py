import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        combos = []  # Stores (lcm, sign)
        
        # Precompute all non-empty subsets using bitmasking or recursion
        def build_combos(idx, count, current_lcm):
            if idx == n:
                if count > 0:
                    # Sign is +1 for odd count, -1 for even count
                    sign = 1 if count % 2 == 1 else -1
                    combos.append((current_lcm, sign))
                return
            
            # Option 1: Exclude coins[idx]
            build_combos(idx + 1, count, current_lcm)
            
            # Option 2: Include coins[idx]
            new_lcm = math.lcm(current_lcm, coins[idx])
            build_combos(idx + 1, count + 1, new_lcm)

        build_combos(0, 0, 1)

        # Fast counting function (O(2^N) per guess using precomputed list)
        def count_multiples(target):
            return sum(target // lcm * sign for lcm, sign in combos)

        # Binary Search over the answer
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans