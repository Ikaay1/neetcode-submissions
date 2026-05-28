# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sorted_list = sorted_temp = ListNode()
        list1_temp = list1
        list2_temp = list2

        while list1_temp and list2_temp:
            list1_val = list1_temp.val
            list2_val = list2_temp.val

            if list1_val < list2_val:
                sorted_temp.next = list1_temp
                list1_temp = list1_temp.next
            else:
                sorted_temp.next = list2_temp
                list2_temp = list2_temp.next
            
            sorted_temp = sorted_temp.next
        
        if list1_temp:
            sorted_temp.next = list1_temp
        else:
            sorted_temp.next = list2_temp
        
        return sorted_list.next