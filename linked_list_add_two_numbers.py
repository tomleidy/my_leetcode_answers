import re
import json
from typing import Optional

# pylint:disable=C0103,R0903,W0613


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int | None = 0, next=None):  # pylint: disable=W0622
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0
    ) -> Optional[ListNode]:
        assert isinstance(l1, ListNode)
        assert isinstance(l2, ListNode)

        return ListNode()  # added to keep Pylance at bay.


if __name__ == "__main__":

    def print_list(node: ListNode) -> None:
        values = []
        current = node
        while current:
            values.append(current.val)
            current = current.next
        output = json.dumps(values)
        output = re.sub(r"[^\d, \[\]]+", "", output)
        output.replace("None", "")
        print(output)

    def make_list(nodes: list) -> ListNode | None:
        if not nodes:
            return None
        if nodes[0] == 0:
            return ListNode(None, make_list(nodes[1:]))
        return ListNode(nodes[0], make_list(nodes[1:]))

    def lists_are_equal(l1: ListNode | None, l2: ListNode | None) -> bool:
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = getattr(l1, "next", None)
            l2 = getattr(l2, "next", None)
        return l1 is None and l2 is None

    cases = {
        1: [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
        2: [[0], [0], []],
        3: [
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9],
            [8, 9, 9, 9, 0, 0, 0, 1],
        ],
    }
    solution = Solution()
    for c in cases.values():
        l1_test = make_list(c[0])
        l2_test = make_list(c[1])
        assert isinstance(l1_test, ListNode)
        expect = make_list(c[2])
        result = solution.addTwoNumbers(l1_test, l2_test)
        print(lists_are_equal(result, expect))
