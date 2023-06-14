# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        adding = 0

        while l1 or l2:

            adding, cur.val = divmod(
                ((l1.val if l1 else 0) + 
                (l2.val if l2 else 0) + 
                adding),
                10,
            )
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            if l1 or l2:
                cur.next = ListNode()
                cur = cur.next
        if adding > 0:
            cur.next = ListNode(adding)

        return res
        