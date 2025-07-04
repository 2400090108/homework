# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pointerA, pointerB = headA, headB
        while pointerA is not pointerB:
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next

        return pointerA
