# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_a = head
        node_b = head.next
        while node_b:
            num = math.gcd(node_a.val, node_b.val)
            node = ListNode(num)
            node_a.next = node
            node.next = node_b
            node_a = node_b
            node_b = node_b.next
        return head