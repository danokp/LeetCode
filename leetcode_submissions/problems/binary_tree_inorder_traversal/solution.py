# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def inner(root, result):
            if root:
                inner(root.left, result)
                result.append(root.val)
                inner(root.right, result)
                return result

        return inner(root, result)