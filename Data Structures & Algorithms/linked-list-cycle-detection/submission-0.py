# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hashSet = set()
        temp = head

        while temp:
            if temp in hashSet:
                return True
            hashSet.add(temp)
            temp = temp.next
        
        return False