from collections import defaultdict

class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = defaultdict(int)
        bracket_map['['] = ']'
        bracket_map['{'] = '}'
        bracket_map['('] = ')'

        stack = []

        for char in s:
            if bracket_map[char] != 0:
                stack.append(char)
            elif stack:
                if bracket_map[stack.pop()] == char:
                    continue
                else:
                    return False
            else:
                return False

        if stack:
            return False
        else:
            return True               