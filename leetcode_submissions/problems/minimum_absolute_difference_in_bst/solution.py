# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inner(node, lst):
            if node is None:
                return None
            inner(node.left, lst)
            lst.append(node.val)
            inner(node.right, lst)
            return lst
        
        node_lst = inner(root, [])
        min_dist = float('inf')

        for i in range(len(node_lst)-1):
            min_dist = min(min_dist, node_lst[i+1]-node_lst[i])
        return min_dist


