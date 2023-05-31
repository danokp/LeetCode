# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def inner(left_root, right_root):
            if left_root is None and right_root is None:
                return True
            if (left_root is None and right_root is not None or
                left_root is not None and right_root is None):
                return False
            if left_root.val == right_root.val:
                return inner(left_root.left, right_root.right) and inner(left_root.right, right_root.left)
        
        return inner(root.left, root.right)



        # def inner_left(res, root):
        #     if root:
        #         inner_left(res, root.left)
        #         inner_right(res, root.right)
        #         res.append(root.val)
        #     else:
        #         res.append(None)
        #     return res

        # def inner_right(res, root):
        #     if root:
        #         inner_right(res, root.right)
        #         inner_right(res, root.left)
        #         res.append(root.val)
        #     else:
        #         res.append(None)
        #     return res
        
        # return inner_left([], root.left) == inner_right([], root.right)
