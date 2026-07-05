class Solution:
    def climbStairs(self, n: int) -> int:
       paths = [0,1,2]
       if n>2:
        for i in range(3,n):
            paths.append(0)  
            paths[i] = paths[i-1] + paths[i-2]
        return paths[-1] + paths[-2] 
       else:
        return paths[n]  
           