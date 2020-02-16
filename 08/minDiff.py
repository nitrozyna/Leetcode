class Solution:

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 999
        count = []
        for i in range(0, len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                count = []
            if diff == min_diff:
                count.append([arr[i], arr[i + 1]])

        return count