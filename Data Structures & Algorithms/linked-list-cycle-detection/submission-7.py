# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

            if(head != None):
                fast_ptr = head
                while(True):
                    head = head.next
                    if head == None:
                        break
                    fast_ptr = fast_ptr.next.next
                    if fast_ptr == None:
                        break
                    elif fast_ptr == head:
                        return True      
            return False    