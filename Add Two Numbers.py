# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)   # Placeholder node to simplify building the result list
        current = dummy       # Pointer to build the result
        carry = 0             # Carry to pass to the next digit

        # Continue as long as there are digits left OR a carry remains
        while l1 or l2 or carry:

            # Get the digit value (0 if the list has ended)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add digits + carry
            total = val1 + val2 + carry

            carry   = total // 10   # e.g. total=17 → carry=1
            digit   = total % 10    # e.g. total=17 → digit=7

            # Append the digit as a new node
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes (if they exist)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next   # Skip the dummy head, return the real result
