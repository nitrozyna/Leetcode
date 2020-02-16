class Solution:

    # recursion, repeating calculations
    def climbStairs1(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs1(n - 1) + self.climbStairs1(n - 2)

    def climbStairs2(self, n: int) -> int:
        return self.helper(n, {})

    # Memoization and a top down approach which makes it O(n) time and O(n) space
    def helper(self, n, cache):
        if n in cache:
            return cache[n]
        if n <= 2:
            return n
        res = self.helper(n - 1, cache) + self.helper(n - 2, cache)
        cache[n] = res
        return res