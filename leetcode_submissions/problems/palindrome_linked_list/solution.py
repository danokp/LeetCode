# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        prev = None
        cur = slow
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
            
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

