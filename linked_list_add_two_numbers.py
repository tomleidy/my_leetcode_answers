import re
import json
from typing import Optional
import time

# https://leetcode.com/problems/add-two-numbers/submissions/1783642979/
# pylint:disable=C0103,R0903,W0613


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):  # pylint: disable=W0622
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # value summing
        next_1 = getattr(l1, "next", None)
        next_2 = getattr(l2, "next", None)
        v_sum = getattr(l1, "val", 0) + getattr(l2, "val", 0)

        # carrying math
        carry = 0
        if v_sum > 9:
            carry = int(v_sum / 10)
            v_sum = v_sum % 10

        # recursion
        if next_1 or next_2:
            if carry > 0:
                if next_1:
                    l1.next.val += carry
                else:
                    l2.next.val += carry
            return ListNode(v_sum, self.addTwoNumbers(next_1, next_2))
        if carry > 0:
            return ListNode(v_sum, ListNode(carry))
        return ListNode(v_sum)


if __name__ == "__main__":

    def get_listnode_as_str(node: ListNode) -> str:
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
        if not nodes:
            return None
        if nodes[0] == 0:
            return ListNode(0, make_list(nodes[1:]))
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
        2: [[0], [0], [0]],
        3: [
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9],
            [8, 9, 9, 9, 0, 0, 0, 1],
        ],
    }
    solution = Solution()
    all_start = time.perf_counter()
    for c in cases.values():
        l1_test = make_list(c[0])
        l2_test = make_list(c[1])
        # assert isinstance(l1_test, ListNode)
        expect = make_list(c[2])
        start = time.perf_counter()
        result = solution.addTwoNumbers(l1_test, l2_test)
        end = time.perf_counter()
        # print(lists_are_equal(result, expect))
        # print(f"Loop time: {end - start} seconds\n")
        # i1 = get_listnode_as_str(l1_test)
        # i2 = get_listnode_as_str(l2_test)
        # r = get_listnode_as_str(result)
        # e = get_listnode_as_str(expect)
        # print(f"{i1=}\n{i2=}")
        # print(f"{r=}\n{e=}\n")
    all_end = time.perf_counter()
    print(f"Total time: {all_end - all_start} seconds\n")
