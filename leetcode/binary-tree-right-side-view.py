# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        queue = deque()
        retList = []

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            level_length = len(queue)
            for i in range(level_length):
                curr = queue.popleft()
                if i == 0:
                    retList.append(curr.val)
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
        return retList