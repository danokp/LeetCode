# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        elif p or q:
            return False
        return True
        
        # if p.val == q.val:
        #     if p.left and q.left:
        #         return self.isSameTree(p.left, q.left)
        #     elif p.left or q.left:
        #         return False
        #     if p.right and q.right:
        #         return self.isSameTree(p.right, q.right)
        #     elif p.right or q.right:
        #         return False
        #     return True           
        # else:
        #     return False

        