import math


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)
        percent = math.ceil(size * 0.25)
        num_dict = {}
        if size == 1:
            return arr[0]
        for e in arr:
            if e in num_dict:
                if num_dict[e] == percent:
                    return e
                num_dict[e] += 1
            else:
                num_dict[e] = 1





