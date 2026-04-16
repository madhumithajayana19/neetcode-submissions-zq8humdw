class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        t1=sorted(t)
        if (len(s1)==len(t1)):
            if (s1==t1):
                return True
        return False