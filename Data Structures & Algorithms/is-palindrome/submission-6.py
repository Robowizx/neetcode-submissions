class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(_.lower() for _ in s if _.isalnum())
        fwd_ptr = 0
        bwd_ptr = len(s)-1

        while(fwd_ptr < len(s) and bwd_ptr >=0):
            if s[fwd_ptr] != s[bwd_ptr]:
                return False
            fwd_ptr+=1
            bwd_ptr-=1    

        return True    
        
        