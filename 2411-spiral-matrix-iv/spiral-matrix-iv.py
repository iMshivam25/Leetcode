class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        arr = [[-1]*n for _ in range(m)]
        top, bottom, left, right = 0, m - 1, 0, n - 1
        i, j = 0, 0
        direction = 0  # 0 - right, 1 - down, 2 - left, 3 - up
        
        while head:
            arr[i][j] = head.val
            head = head.next
            
            if direction == 0:  # Moving right
                if j < right:
                    j += 1
                else:  # Change direction to down
                    direction = 1
                    top += 1
                    i += 1
            elif direction == 1:  # Moving down
                if i < bottom:
                    i += 1
                else:  # Change direction to left
                    direction = 2
                    right -= 1
                    j -= 1
            elif direction == 2:  # Moving left
                if j > left:
                    j -= 1
                else:  # Change direction to up
                    direction = 3
                    bottom -= 1
                    i -= 1
            elif direction == 3:  # Moving up
                if i > top:
                    i -= 1
                else:  # Change direction to right
                    direction = 0
                    left += 1
                    j += 1

        return arr
