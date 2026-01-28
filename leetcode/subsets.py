class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])
        return subsets