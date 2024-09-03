class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''.join(str(ord(ch) - ord('a') + 1) for ch in s)
        total_sum = sum(int(digit) for digit in num_str)
        for _ in range(k-1):
            temp = total_sum
            total_sum = 0
            while temp>0:
                total_sum += temp%10
                temp//= 10
        return total_sum