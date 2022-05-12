class Solution:
    def maxSearch(self, node: TreeNode, maxVal):
        if not node:
            return 0
        
        maxVal = node.val if node.val >= maxVal else maxVal
        lGoodNodes = self.maxSearch(node.left, maxVal) # left search
        rGoodNodes = self.maxSearch(node.right, maxVal) # left search
        return lGoodNodes + rGoodNodes + 1 if maxVal == node.val else lGoodNodes + rGoodNodes
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.maxSearch(root, root.val)