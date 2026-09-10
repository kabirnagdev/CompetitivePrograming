class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #k speed 
        def possible(k) -> bool:
            hrs = []
            for i in piles :
                hrs.append(int((i-1)/k+1))
                
            if(sum(hrs)) <= h:
                return True
   

        left, right = 1 , max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        # k = 1
        # while True:
        #     hours = 0

        #     for i in piles:
        #         hours += int((i-1)/k+1)

        #     if hours <= h:
        #         return k

        #     k += 1