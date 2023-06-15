# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        def inner(node, depth):
            if node is None:
                return
            sum_store_dct[depth] = sum_store_dct.get(depth, 0) + node.val
            depth += 1
            inner(node.left, depth)
            inner(node.right, depth)

        sum_store_dct = {}
        inner(root, 1)
        max_val_depth = (float('-inf'), float('inf'))
        for k, v in sum_store_dct.items():
            if v > max_val_depth[0] or (v == max_val_depth[0] and k < max_val_depth[1]):
                max_val_depth = (v, k)
        return max_val_depth[1]
