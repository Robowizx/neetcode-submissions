# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameter(self, root: Optional[TreeNode]) -> tuple:
            
        if not root or (root.left == None and root.right == None):
            return (0,0)

        sub_right = self.diameter(root.right)
        sub_left = self.diameter(root.left)
        children = (0 if root.right==None else 1) + (0 if root.left==None else 1)
        max_path = max((children+sub_right[1]+sub_left[1]),max(sub_right[0],sub_left[0]))
        max_depth = 1+max(sub_right[1],sub_left[1])

        print(f'{root.val} -> ({max_path},{max_depth})')
        return (max_path,max_depth)
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        out = self.diameter(root)
        return out[0]