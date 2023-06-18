# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def inner(node, path):
            path += str(node.val) + '->'
            if node.left is None and node.right is None:
                ans.append(path[:-2])
            if node.left:
                inner(node.left, path)
            if node.right:
                inner(node.right, path)  
        inner(root, '')
        return ans