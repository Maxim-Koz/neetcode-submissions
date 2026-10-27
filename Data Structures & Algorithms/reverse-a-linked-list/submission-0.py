# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current is not None:
            temp_next = current.next
            if current == head:
                current.next = None
            else:
                current.next = prev
            prev = current
            current = temp_next
        return prev