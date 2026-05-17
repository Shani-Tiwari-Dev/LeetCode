class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if there's only 1 row, or rows exceed string length, no zigzag happens
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of strings for each row
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through each character in the string
        for char in s:
            rows[current_row] += char
            
            # Change direction if we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down based on the direction flag
            current_row += 1 if going_down else -1
            
        # Combine all rows together to form the final string
        return "".join(rows)
