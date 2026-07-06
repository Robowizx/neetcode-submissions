class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       num_set = {}

       for i in range(0,len(nums)):
        if nums[i] not in num_set:
            num_set[nums[i]] = [i]
        else:
            num_set[nums[i]].append(i)    

       for i in range(0,len(nums)):
        sub_target = target - nums[i]
        if sub_target in num_set:
            if sub_target != nums[i]:
                return [i,num_set[sub_target][0]]
            else:
                for x in num_set[sub_target]:
                    if x != i:
                        return [i,x]    
        

