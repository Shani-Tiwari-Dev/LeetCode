class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer boundaries
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        
        # Store the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x > 0:
            # Pop the last digit
            pop = x % 10
            x //= 10
            
            # Check for overflow before multiplying res by 10
            if res > MAX_INT // 10 or (res == MAX_INT // 10 and pop > 7):
                return 0
            # Check for underflow (for negative numbers)
            if sign == -1 and (res > abs(MIN_INT) // 10 or (res == abs(MIN_INT) // 10 and pop > 8)):
                return 0
                
            # Push the digit to the result
            res = res * 10 + pop
            
        return res * sign
