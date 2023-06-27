# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inner(node):
            if node is None:
                return
            inner(node.left)
            ans.append(node.val)
            inner(node.right)
        inner(root)
        return ans
