from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        studs = deque(students)
        sands = deque(sandwiches)
        i = 0
        while i < len(studs):
            if studs[0] == sands[0]:
                studs.popleft()
                sands.popleft()
                i = 0
            else:
                val = studs.popleft()
                studs.append(val)
                i += 1
        return len(studs)