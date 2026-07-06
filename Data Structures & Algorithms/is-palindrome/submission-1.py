class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        fwd_ptr = 0
        bwd_ptr = len(s)-1

        while(fwd_ptr < len(s) and bwd_ptr >=0):
            if not s[fwd_ptr].isalnum():
                fwd_ptr+=1
            elif not s[bwd_ptr].isalnum():
                bwd_ptr-=1
            else:
                if s[fwd_ptr] != s[bwd_ptr]:
                    return False
                else:
                    fwd_ptr+=1
                    bwd_ptr-=1    

        return True    
        
        