class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        curr = 1
        while k > 1:
            # Determine the steps between the current number and the next one in lexicographical order
            steps = 0
            first = curr
            last = curr + 1
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10

            if steps <= k - 1:
                # Skip over this subtree of numbers
                curr += 1
                k -= steps
            else:
                # Go down to the next level of numbers
                curr *= 10
                k -= 1
        return curr
