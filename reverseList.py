# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Define our reference and initialize our previous
        node, prev = head, None
        
        # Traverse through linkedlist and point current node
        # to previous
        while node is not None:
            # Store next node to continue traversal
            next_node = node.next
            # Set current node to point to previous
            node.next = prev
            # Set prev to current node
            prev = node
            # Update pointer to go to next node
            node = next_node
        
        # New head node will be the last previous before None
        return prev