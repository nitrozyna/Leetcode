class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            result = []
        else:
            result = [0]
        tmp = n
        if n >1:
            for i in range(0,n):
                result.append(tmp)
                result.append(-tmp)
                tmp = tmp -1
                if len(result) == n:
                    break
        return result
