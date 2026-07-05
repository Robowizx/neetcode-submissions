class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        while(len(s)>0 and len(t)>0):
            letter = s[0]
            if letter in t:
                s.remove(letter)
                t.remove(letter)
            else:
                return False    

        if len(t) == 0 and len(s) == 0:
            return True
        return False   