# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def inner(count, depth_list, root):
            count += 1
            # print(f'{root.val=}, {root.left=}, {root.right=}')
            # print(f'{root=}')
            if root.left:
                inner(count, depth_list, root.left)
            if root.right:
                inner(count, depth_list, root.right)
            if root.left is None and root.right is None:
                depth_list.append(count)
            return depth_list
        return min(inner(0, [], root)) if root else 0