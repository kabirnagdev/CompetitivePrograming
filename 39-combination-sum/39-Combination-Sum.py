from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, current_combo, current_sum):
            # Base Case 1: If we hit the exact target, save it
            if current_sum == target:
                res.append(list(current_combo))
                return
            # Base Case 2: If we overshoot the target, stop looking down this path
            if current_sum > target:
                return
            
            # Explore further numbers
            for i in range(start, len(candidates)):
                current_combo.append(candidates[i])
                # Notice we pass 'i' instead of 'i + 1' 
                # This is what allows us to reuse the same number multiple times!
                backtrack(i, current_combo, current_sum + candidates[i])
                current_combo.pop() # Undo the choice (backtrack)

        backtrack(0, [], 0)
        return res