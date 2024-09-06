class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for faster lookup
        nums_set = set(nums)

        # Skip all nodes at the start where head.val is in nums_set
        while head and head.val in nums_set:
            head = head.next
        
        # Keep the reference to the new head (start of modified list)
        ans = head
        
        # Traverse the rest of the list
        while head and head.next:
            if head.next.val in nums_set:
                # Skip the node whose value is in nums_set
                head.next = head.next.next
            else:
                # Move to the next node
                head = head.next
        
        return ans
