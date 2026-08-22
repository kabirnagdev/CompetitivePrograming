class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ans = []
        a = set(arr)
        for i in a :
            b =  arr.count(i)
            ans.append(b)
        print(ans)
        for i in ans :
            if ans.count(i) > 1:
                return False
            
        else : return True

        