# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        """
        The following structure utilizes the min heap pattern,
        by forming a sequenced conveyor belt that places
        all of the linked lists into the minimum heap, then
        pops the smallest linked list appends it to a dummy
        list, assigns it back into the minimum heap. Finally
        returns dummy.next
        """
        
        if lists == []: return None

        import heapq
        min_heap = []

        for i, node in enumerate(lists):
            if node == None: continue
            heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next

        # Time Complexity -> O(N log N) as N is the number of elements in k list
        # Space Complexity -> O(1) as the auxillary space remains constant
