# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1== None and list2 == None:
            return None
        elif list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        else:            

            merged_head = ListNode()
            merged_list = merged_head

            while(True):
                if list1.val == list2.val:
                    merged_list.val = list1.val
                    merged_list.next = ListNode(list2.val)
                    list1 = list1.next
                    list2 = list2.next
                    merged_list = merged_list.next
                elif list1.val < list2.val:
                    merged_list.val = list1.val
                    list1 = list1.next
                elif list1.val > list2.val:    
                    merged_list.val = list2.val
                    list2 = list2.next

                if(list1 == None and list2 == None):
                    break
                elif(list1 == None):
                    merged_list.next = list2
                    break
                elif(list2 == None):
                    merged_list.next = list1
                    break
                else:
                    merged_list.next = ListNode()
                    merged_list = merged_list.next                

            return merged_head    

            