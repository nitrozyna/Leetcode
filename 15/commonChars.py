class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        output = []
        for char in A[0]:
            if all(char in string for string in A):
                output.append(char)
                A = [s.replace(char,'',1) for s in A]
        return output