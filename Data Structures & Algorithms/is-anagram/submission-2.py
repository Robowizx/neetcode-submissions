class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        H_map ={}

        for i in range(0,len(s)):

            if s[i] not in H_map:
                H_map[s[i]] = 1
            else:
                H_map[s[i]] = H_map[s[i]] + 1

            if t[i] not in H_map:
                H_map[t[i]] = -1
            else:
                H_map[t[i]] = H_map[t[i]] - 1 
   
 

        for val in H_map.values():
            if val != 0:
                return False             

        return True            
