import itertools
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        u = [list(p) for p in itertools.permutations(digits, 3)]
        u = [int("".join(map(str, sublist))) for sublist in u ]
        a = []
        for i in u :
            if i%2 == 0 and i>99:
                a.append(i)
        print(a)
        return len(set(a))

        
    