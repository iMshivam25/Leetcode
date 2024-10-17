class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of digits
        digits = list(str(num))
        
        # Create a list to store the last occurrence of each digit
        last = {int(d): i for i, d in enumerate(digits)}
        
        # Iterate through each digit in the list
        for i, d in enumerate(digits):
            # Check if a larger digit exists after the current digit
            for digit in range(9, int(d), -1):  # Check for larger digits from 9 down to current digit + 1
                if last.get(digit, -1) > i:  # If a larger digit exists and occurs after current digit
                    # Swap the current digit with the larger digit
                    digits[i], digits[last[digit]] = digits[last[digit]], digits[i]
                    # Convert the list back to an integer and return
                    return int(''.join(digits))
        
        # If no swap was made, return the original number
        return num
