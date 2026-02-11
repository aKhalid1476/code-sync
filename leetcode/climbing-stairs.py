class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashmap = {}

        def helper(i):
            if i > n:
                return 0
            if i in hashmap:
                return hashmap[i]
            if i == n:
                return 1
            hashmap[i] = helper(i + 1) + helper(i + 2)
            return hashmap[i]
        
        return helper(0)