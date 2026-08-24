class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]*(n+1)

        for i in range(0,n+1):
            output[i] = (i&1)+output[i>>1]

        return output    