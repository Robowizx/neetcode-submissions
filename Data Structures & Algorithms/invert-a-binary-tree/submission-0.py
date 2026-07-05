# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        inverted_root = root

        if root!= None:
            stack.append(root)

        while(len(stack)>0):
            node = stack.pop()
            if (node.right!= None or node.left!= None):
                buff = node.right
                node.right = node.left
                node.left = buff
                if node.right!= None:
                    stack.append(node.right)
                if node.left!= None:
                    stack.append(node.left)    

        return inverted_root    