# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        def search(root):
            if root:
                search(root.left)
                vals.append(root.val)
                search(root.right)
        search(root)


        def intobst(vals):
            if not vals:
                return None
            mid = len(vals)//2
            root = TreeNode(vals[mid])
            root.left = intobst(vals[:mid])
            root.right = intobst(vals[mid+1:])
            return root
        return intobst(vals)

        