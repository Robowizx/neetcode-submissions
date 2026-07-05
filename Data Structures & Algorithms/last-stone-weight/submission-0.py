class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            x = stones.pop()
            y = stones.pop()
            z = x-y

            if z:
                flag = False
                for i,n in enumerate(stones):
                    if n > z:
                        stones.insert(i,z)
                        flag = True
                        break
                if not flag:
                    stones.append(z)

        if len(stones):
            return stones[0]
        else:
            return 0            