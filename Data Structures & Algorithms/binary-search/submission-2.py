import math 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        beg = 0
        end = len(nums)-1

        while(end >= beg):
            pos = (end+beg)//2

            if nums[pos] == target:
                return pos
            elif nums[pos] > target:
                end = pos-1
            else:
                beg = pos+1

        return -1            
