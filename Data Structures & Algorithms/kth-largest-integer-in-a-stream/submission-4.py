class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums.copy()
        self.nums.sort(reverse=True)

    def add(self, val: int) -> int:
      
       if len(self.nums):
            flag = False
            for i,n in enumerate(self.nums):
                if n < val:
                    self.nums.insert(i,val)
                    flag = True
                    break
            if not flag:
                self.nums.append(val)        
       else:
            self.nums.append(val)         

       return self.nums[self.k-1]
        