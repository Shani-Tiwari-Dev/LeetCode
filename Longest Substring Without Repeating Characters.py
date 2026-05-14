class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the last seen index of each character
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If we've seen the character and it's inside our current window
            if char in char_map and char_map[char] >= left:
                # Move the left pointer to the right of the previous occurrence
                left = char_map[char] + 1
            
            # Update the character's last seen position
            char_map[char] = right
            
            # Calculate the current window size and update max_length
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)
            
        return max_length
