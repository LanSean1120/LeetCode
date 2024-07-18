# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = [0]
        def sol(root) -> list:
            if not root:
                return [0]
            if not root.left and not root.right:
                return [1]
            res = []
            right = sol(root.right)
            left = sol(root.left)
            for i in right:
                for j in left:
                    if i!=0 and j!=0 and i+j <= distance:
                        ans[0] += 1
            for i in right:
                if i>0:
                    res.append(i+1)
            for j in left:
                if j > 0:
                    res.append(j+1)
            return res
        
        sol(root)
        return ans[0]