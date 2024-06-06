# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def sol(root):
            if root:
                left = sol(root.left)
                right = sol(root.right)
                nonlocal ans
                ans += abs(left)+abs(right)
                return root.val+left+right-1
            return 0
        ans = 0
        sol(root)
        return ans
        