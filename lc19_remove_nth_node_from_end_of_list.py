import re
import json
from typing import Optional
import time
import sys

# pylint:disable=C0103,R0903,W0613


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # pylint: disable=W0622
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass


if __name__ == "__main__":

    def get_listnode_as_str(node: ListNode | None) -> str:
        """Get ListNode values as a string resembling a list"""
        values = []
        current = node
        while current:
            values.append(current.val)
            current = current.next
        output = json.dumps(values)
        output = re.sub(r"[^\d, \[\]]+", "", output)
        output.replace("None", "")
        return output

    def make_list(nodes: list) -> ListNode | None:
        """Generate linked list based on list parameter"""
        if not nodes:
            return None
        if nodes[0] == 0:
            return ListNode(0, make_list(nodes[1:]))
        return ListNode(nodes[0], make_list(nodes[1:]))

    def lists_are_equal(l1: ListNode | None, l2: ListNode | None) -> bool:
        """Compare two lists"""
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = getattr(l1, "next", None)
            l2 = getattr(l2, "next", None)
        return l1 is None and l2 is None

    def pass_not_pass(l1: ListNode | None, l2: ListNode | None) -> str:
        """Wrapper for lists_are_equal() for testing output"""
        if lists_are_equal(l1, l2):
            return "Pass"
        return "ERROR"

    # Test cases, each sublist is [head, n, expected]
    cases = {
        1: [[1, 2, 3, 4, 5], 2, [1, 2, 3, 5]],
        2: [[1], 1, []],
        3: [[1, 2], 1, [1]],
        4: [[1, 2], 2, [2]],
    }
    solution = Solution()

    round_times = []
    try:
        for i, c in enumerate(cases.values()):
            h_list = make_list(c[0])
            n_value = c[1]
            expect = make_list(c[2])
            start = time.perf_counter()
            result = solution.removeNthFromEnd(h_list, n_value)
            end = time.perf_counter()
            round_times.append(end - start)

            e = get_listnode_as_str(expect)
            r = get_listnode_as_str(result)
            print(
                f"Test {i}:",
                pass_not_pass(result, expect),
                f"(result: {r}, expected: {e})",
            )

        print(f"Total time: {sum(round_times)} seconds\n")
    except KeyboardInterrupt:
        print()
        sys.exit(1)
