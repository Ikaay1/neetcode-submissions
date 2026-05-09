# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def get_length():
            length = 0
            temp = head

            while temp:
                length += 1
                temp = temp.next
            
            return length

        def reverse(node):

            prev = None
            temp = node

            while temp:
                keep = temp.next
                temp.next = prev
                prev = temp
                temp = keep
            
            return prev
        
        # def print_node(node):
        #     temp = node

        #     while node:
        #         print(node.val)
        #         node = node.next
            
        #     print("-------")
        
        list_len = get_length()
        mid_point = list_len // 2
        temp = first_half = head
        count = 1

        while count < mid_point:
            temp = temp.next
            count += 1
        
        second_half = reverse(temp.next)
        temp.next = None
        res = res_temp = ListNode()
        # print_node(first_half)
        # print_node(second_half)

        while first_half and second_half:
            res_temp.next = first_half
            res_temp = res_temp.next
            first_half = res_temp.next
            res_temp.next = second_half
            res_temp = res_temp.next
            second_half = res_temp.next
        
        # return res
