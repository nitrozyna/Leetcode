class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if sum(A) % 3 != 0:
            return False
        res = sum(A) // 3
        count = 0
        parts = 0
        for i in range(len(A)):
            count += A[i]
            if count == res:
                parts += 1
                if parts == 3:
                    return True
                count = 0
        return False
        
