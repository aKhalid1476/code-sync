# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        if not root:
            return []
        arr.extend(self.inorderTraversal(root.left))
        arr.append(root.val)
        arr.extend(self.inorderTraversal(root.right))
        return arr