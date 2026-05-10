# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_temp = l1
        l2_temp = l2
        remainder = 0
        res = res_temp = ListNode()

        while l1_temp or l2_temp or remainder:
            l1_val = l1_temp.val if l1_temp else 0
            l2_val = l2_temp.val if l2_temp else 0
            addition = l1_val + l2_val + remainder
            value_to_store = addition % 10
            remainder = addition // 10

            res_temp.next = ListNode(value_to_store)
            res_temp = res_temp.next
            if l1_temp:
                l1_temp = l1_temp.next
            if l2_temp:
                l2_temp = l2_temp.next

        
        return res.next

