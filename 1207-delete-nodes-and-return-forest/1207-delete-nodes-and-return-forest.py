# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        def postorder(root):
            if not root:
                return 
            root.left = postorder(root.left)
            root.right = postorder(root.right)
            if root.val in to_delete:
                if root.left:
                    ans.append(root.left)
                    
                if root.right:
                    ans.append(root.right)
                root = TreeNode()
                return root.left
            return root


            
        postorder(root)
        if root.val not in to_delete:
            ans.append(root)
        return ans