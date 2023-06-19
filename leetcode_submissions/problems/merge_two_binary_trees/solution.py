# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inner(root1, root2, root_merged):
            if not root1 and not root2:
                return
            root1 = root1 or TreeNode(0)
            root2 = root2 or TreeNode(0)
            # print(f'{root1.val=}, {root2.val=}')
            root_merged.val = root1.val + root2.val
            if root1.left or root2.left:
                root_merged.left = TreeNode()
                inner(root1.left, root2.left, root_merged.left)
            if root1.right or root2.right:
                root_merged.right = TreeNode()
                inner(root1.right, root2.right, root_merged.right)
        if  root1 or root2:
            root_merged = TreeNode()
            inner(root1, root2, root_merged)
            return root_merged
        return