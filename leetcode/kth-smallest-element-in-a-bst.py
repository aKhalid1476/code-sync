# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    cnt = 0
    val = 0
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.helper(root, k)
        self.cnt = 0
        return self.val
    
    def helper(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: None
        """
        if not root:
            return
        
        self.helper(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.val = root.val
        self.helper(root.right, k)