class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        node_count = 0
        node = head
        while node:
            node_count += 1
            node = node.next
        rem = node_count % k
        part_size = node_count//k
        curr = head
        for i in range(k):
            part_head = curr
            curr_part_size = part_size + (1 if i<rem else 0)
            for j in range(curr_part_size-1):
                if curr:
                    curr = curr.next
            if curr:
                next_part_head = curr.next
                curr.next = None
                curr = next_part_head
            ans.append(part_head)
                  
        return ans
        