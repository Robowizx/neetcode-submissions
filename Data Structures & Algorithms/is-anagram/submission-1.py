class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        S_map = {}
        T_map = {}

        def create_map(s: str, map: dict):

            for char in s:
                if char in map:
                    map[char] += 1
                else:
                    map[char] = 1 

        create_map(s,S_map)
        create_map(t,T_map)

        for key in S_map.keys():
            if key not in T_map:
                return False
            elif S_map[key] != T_map[key]:
                return False

        return True            
