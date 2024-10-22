from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode() 
        current = dummy_head  
        carry = 0 
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            current.next = ListNode(new_val)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next
def print_linked_list(node: Optional[ListNode]):
    current = node
    while current:
        print(current.val, end = " -> ")
        current = current.next
    print("None")
def create_linked_list(lst):
    dummy_head = ListNode()
    current = dummy_head
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy_head.next

l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)