# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Define our result linked list
        head = None
        # Reference of head
        temp = None
        # Default our carry value to zero
        carry = 0
        # Iterarate through both list
        while l1 is not None or l2 is not None:
            # Add carry on each iteration as we traverse
            sum_val = carry
            # Add l1 value to variable with carry and update pointer
            if l1 is not None:
                sum_val += l1.val
                l1 = l1.next
            # Add l2 value to variable with carry and update pointer
            if l2 is not None:
                sum_val += l2.val
                l2 = l2.next
            # Create a temp result node for the sum of the values
            # from both list, take modulus
            tnode = ListNode(sum_val % 10)
            # Update carry value for next iteration
            carry = sum_val // 10
            # Initial node condition
            if temp == None:
                temp = tnode
                head = tnode
            else:
                temp.next = tnode
                temp = temp.next
        # Check for remaining carry values
        if carry > 0:
            temp.next = ListNode(carry)
        # Return head of result linked list
        return head
            