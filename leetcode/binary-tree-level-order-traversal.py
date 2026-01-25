# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = deque()
        retList = []
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            listToAppend = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                listToAppend.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            retList.append(listToAppend)
        
        return retList