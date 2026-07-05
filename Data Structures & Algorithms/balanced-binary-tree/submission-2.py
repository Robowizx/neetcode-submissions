# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getBalance(source: Optional[TreeNode]) -> tuple:
            
               if not source:
                    print((0,True))
                    return (0,True)

               print(source.val)
               left_sub = getBalance(source.left)
               right_sub = getBalance(source.right)

               if not (left_sub[1] and right_sub[1]):
                    print((-1,False))
                    return (-1,False)
               elif abs(left_sub[0] - right_sub[0]) > 1:

                    print(f'{(-1,False)} --- diff = {abs(left_sub[0] - right_sub[0])}')
                    return (-1,False)
               else:
                    print ((1+max(left_sub[0],right_sub[0]),True))
                    return (1+max(left_sub[0],right_sub[0]),True)                 

        return getBalance(root)[1]          