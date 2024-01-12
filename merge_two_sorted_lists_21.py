"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_node = ListNode(0)

        result = merge_node

        while list1 and list2:
            if list1.val < list2.val:
                merge_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merge_node.next = ListNode(list2.val)
                list2 = list2.next

            merge_node = merge_node.next

        while list1:
            merge_node.next = ListNode(list1.val)
            list1 = list1.next
            merge_node = merge_node.next

        while list2:
            merge_node.next = ListNode(list2.val)
            list2 = list2.next
            merge_node = merge_node.next

        return result.next

def create_linked_list(lst):
    head = ListNode(0)
    current = head
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return head.next

def to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

if __name__ == '__main__':
    solution = Solution()

    assert to_list(solution.mergeTwoLists(create_linked_list([1, 2, 4]), create_linked_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4], "Error on test case 1"
    assert to_list(solution.mergeTwoLists(create_linked_list([]), create_linked_list([]))) == [], "Error on test case 2"
    assert to_list(solution.mergeTwoLists(create_linked_list([]), create_linked_list([0]))) == [0], "Error on test case 3"

    print("All tests passed successfully.")