# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()        
        def inner(root, num_lst):
            mid_index = len(num_lst) // 2
            root.val = num_lst[mid_index]
            if len(num_lst) == 0:
                return
            if len(num_lst[:mid_index]) > 0:
                root.left = TreeNode()
                inner(root.left, num_lst[:mid_index])
            if len(num_lst[mid_index+1:]) > 0:
                root.right = TreeNode()
                inner(root.right, num_lst[mid_index+1:])
        inner(root, nums)
        return root