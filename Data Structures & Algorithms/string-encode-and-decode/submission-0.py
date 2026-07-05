class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for word in strs:
            out += str(len(word))+'#'+word
        return out    

    def decode(self, s: str) -> List[str]:
        strs = []
        string_buffer = ''
        i = 0
        while (i<len(s)):
            if s[i] != '#':
                string_buffer += s[i]
                i+=1
            else:
                print(string_buffer)
                strs.append(s[i+1:i+1+int(string_buffer)])
                i+=int(string_buffer)+1
                string_buffer = '' 
        return strs        
