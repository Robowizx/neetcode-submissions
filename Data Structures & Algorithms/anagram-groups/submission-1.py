class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def isAnagram(s:str,t:str) -> bool:
            if len(s) != len(t):
                return False

            countS , countT = {} , {}

            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i],0)
                countT[t[i]] = 1 + countT.get(t[i],0)
            return countS == countT

        result = []
        
        while(len(strs)>0):
            sublist = [strs[0]]
            pos=1
            while(pos<len(strs)):
                if isAnagram(strs[0],strs[pos]):
                    sublist.append(strs[pos])
                    strs.pop(pos)
                else:
                    pos+=1
            result.append(sublist)
            strs.pop(0)

        return result               
