# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def sol(node):
            if node == None:
                return node
            node.left = sol(node.left)
            node.right = sol(node.right)
            if node.right==None and node.left == None and node.val == target:
                return  None
            return node
        return sol(root)
        