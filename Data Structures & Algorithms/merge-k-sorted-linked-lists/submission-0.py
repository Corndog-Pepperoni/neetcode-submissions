import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # create min heap which takes every first element of each linked list
        # add the first element value and the node (represents the linked list) to the heap
        # while the heap has values
        # take the list with the smallest first element and add it to the result list
        # increment to node.next and put that new node and its value back into the heap
        # keep doing this process until every linked list is exhausted and there are no elements in the heap
        # return the result
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
            
        result = ListNode("result")
        curr = result

        while min_heap:
            curr_val, curr_idx, curr_node = heapq.heappop(min_heap)
            curr.next = ListNode(curr_val)
            curr = curr.next

            if curr_node.next:
                heapq.heappush(min_heap, (curr_node.next.val, curr_idx, curr_node.next))
                
        return result.next
