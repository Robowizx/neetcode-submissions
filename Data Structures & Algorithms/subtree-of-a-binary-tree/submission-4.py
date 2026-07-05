# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subroots = self.searchSubRoot(root,subRoot)

        for candidate in subroots:
            flag = True
            main_traverse = [candidate]
            non_main_traverse = [subRoot]
            
            while (len(non_main_traverse) != 0 and len(main_traverse) != 0):
                
                ptr1 = main_traverse.pop(0)
                ptr2 = non_main_traverse.pop(0)

                if ptr1.val != ptr2.val:
                    flag = False
                    break
                if ptr1.right:
                    main_traverse.append(ptr1.right)
                if ptr1.left:
                    main_traverse.append(ptr1.left)
                if ptr2.right:
                    non_main_traverse.append(ptr2.right)
                if ptr2.left:
                    non_main_traverse.append(ptr2.left)            

            if flag and len(main_traverse) == 0 and len(non_main_traverse) == 0:
                return True        

        return False

    def searchSubRoot(self, root: Optional[TreeNode], node: Optional[TreeNode]) -> list[TreeNode]:
        search_space = [root]
        result = []
        while (len(search_space) != 0):
            pointer = search_space.pop(0)
            if pointer.val == node.val:
                result.append(pointer)
            if pointer.right:
                search_space.append(pointer.right)
            if pointer.left:        
                search_space.append(pointer.left)

        return  result    