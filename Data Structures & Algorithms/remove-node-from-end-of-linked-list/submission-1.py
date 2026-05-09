# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_length():
            length = 0
            temp = head

            while temp:
                length += 1
                temp = temp.next
            
            return length

        list_len = get_length()
        target = list_len - n
        count = 1
        temp = head

        if target == 0:
            return head.next

        while count < target:
            temp = temp.next
            count += 1

        temp.next = temp.next.next

        return head