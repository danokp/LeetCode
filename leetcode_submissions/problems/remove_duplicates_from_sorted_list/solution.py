# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            new_head = head

            while new_head.next:
                if new_head.next.val == new_head.val:
                    new_head.next = new_head.next.next
                else:
                    new_head = new_head.next
        return head