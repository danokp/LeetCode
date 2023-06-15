# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def inner(node, depth):
            if node is None:
                return
            sum_store_dct[depth] = sum_store_dct.get(depth, 0) + node.val
            depth += 1
            inner(node.left, depth)
            inner(node.right, depth)

        sum_store_dct = {}
        inner(root, 1)
        print(sum_store_dct)
        print(sorted(sum_store_dct, key=sum_store_dct.get))

        return sorted(sum_store_dct.values())[-k] if len(sum_store_dct) >= k else -1
        
        