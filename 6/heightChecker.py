class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        comp = sorted(heights)
        count = 0
        for i in range(0,len(heights)):
            if heights[i] != comp[i]:
                count += 1
        return count
