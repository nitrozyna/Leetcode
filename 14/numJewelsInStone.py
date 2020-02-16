class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            for j in J:
                if j == s:
                    count += 1
        return count