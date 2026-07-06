class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       num_set = {}

       for i in range(0,len(nums)):
        diff = target - nums[i]
        if diff in num_set:
            return [num_set[diff],i]
        else:
            num_set[nums[i]] = i      
        

