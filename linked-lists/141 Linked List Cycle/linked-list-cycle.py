# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head: return None

        i = 0
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        
        return False

    # Time Complexity: O(n) -> where n is the number of elements in head
    # Space Complexity: O(1) -> where all auxillery space remains constant
