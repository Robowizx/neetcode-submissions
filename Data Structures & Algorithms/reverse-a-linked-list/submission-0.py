# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        reverse_head = None
        
        while(head != None):
            stack.append(head.val)
            head = head.next

        print(stack)

        if (len(stack)>0):
            reverse_list = ListNode()
            reverse_head = reverse_list
            while(True):
                reverse_list.val = stack.pop()
                if (len(stack)>0):
                    reverse_list.next = ListNode()
                    reverse_list = reverse_list.next
                else:
                    break

        return reverse_head                  

   
    