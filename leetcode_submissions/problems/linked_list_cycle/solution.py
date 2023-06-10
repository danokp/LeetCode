# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev_nodes = []
        node = head
        while node:
            if node in prev_nodes:
                return True
            prev_nodes.append(node)
            node = node.next
        return False
