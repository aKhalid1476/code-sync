# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # base case, figure out later
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # recursive step
        m = len(lists) // 2
        leftHalf = self.mergeKLists(lists[0:m])
        rightHalf = self.mergeKLists(lists[m:])

        # merge step
        ptr1 = leftHalf
        ptr2 = rightHalf
        head = None
        cur = None

        if not ptr1: return ptr2
        if not ptr2: return ptr1

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                if not head:
                    head = ptr1
                    cur = ptr1
                else:
                    cur.next = ptr1
                    cur = cur.next
                ptr1 = ptr1.next
            else:
                if not head:
                    head = ptr2
                    cur = ptr2
                else:
                    cur.next = ptr2
                    cur = cur.next
                ptr2 = ptr2.next

        if ptr1 and not ptr2:
            cur.next = ptr1
        elif ptr2 and not ptr1:
            cur.next = ptr2
        
        return head