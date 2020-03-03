class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = ""
        for i in range(int(len(s)/2)):
            sub += s[i]
            x = int(len(s)/len(sub))
            if((sub)*x == s):
                return True
        return False