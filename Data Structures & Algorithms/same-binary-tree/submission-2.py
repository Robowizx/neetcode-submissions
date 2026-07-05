# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p and q :
            stack_p , stack_q = [p] , [q]
            while(len(stack_p)> 0 and len(stack_q)>0):
                node_p , node_q = stack_p.pop() , stack_q.pop()
                
                if node_p.val != node_q.val:
                    return False

                if (node_p.right and node_q.right):
                        stack_p.append(node_p.right)
                        stack_q.append(node_q.right)
                elif(node_p.right or node_q.right):
                    return False 

                if (node_p.left and node_q.left):
                        stack_p.append(node_p.left)
                        stack_q.append(node_q.left)
                elif (node_p.left or node_q.left):
                    return False          

            if len(stack_p) != len(stack_q):
                return False
            else:
                return True        
        elif p or q:
            return False
        else:
            return True    

