class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countMap = {}

        for num in nums:
            countMap[num] = 1 + countMap.get(num,0)

        countMap = dict(sorted(countMap.items(),key=lambda item: item[1],reverse=True))

        return list(countMap.keys())[0:k]    