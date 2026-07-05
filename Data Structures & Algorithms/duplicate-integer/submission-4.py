class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        uniq = {}

        for num in nums:
            if num in uniq:
                return True
            else:
                uniq[num] = 1

        return False           