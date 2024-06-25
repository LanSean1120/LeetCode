# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        l = []
        def reverse_inorder(root):
            if root:
                reverse_inorder(root.right)
                l.append(root.val)
                root.val = sum(l)
                reverse_inorder(root.left)
        reverse_inorder(root)
        return root
