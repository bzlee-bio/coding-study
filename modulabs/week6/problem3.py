# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        resL = self.dfs(node.left)
        resR = self.dfs(node.right)

        if node.left:
            resL = resL + 1 if node.left.val == node.val else 0
        if node.right:
            resR = resR + 1 if node.right.val == node.val else 0
        
        self.max = max(self.max,  resL+resR)
        return max(resL, resR)
            

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        _ = self.digger(root)
        
        return self.max