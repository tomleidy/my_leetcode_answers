import re
import json
from typing import Optional, List

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
        v_sum = 0
        for x in [l1, l2]:
            val = getattr(x, "val", 0)
            if val:
                v_sum += val

        # carrying math
        if v_sum > 9:
            value = v_sum % 10
            carry = int(v_sum / 10)
        else:
            value = v_sum
            carry = 0

        nexts = [getattr(x, "next", None) for x in [l1, l2]]
        for n in nexts:
            if n:
                n.val += carry
                break
        # recursion
        nodes_left = any(getattr(x, "next", False) for x in [l1, l2])
        if nodes_left:
            return ListNode(value, self.addTwoNumbers(*nexts))
        if carry > 0:
            return ListNode(value, ListNode(carry))

        return ListNode(value)


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
    for c in cases.values():
        l1_test = make_list(c[0])
        l2_test = make_list(c[1])
        assert isinstance(l1_test, ListNode)
        expect = make_list(c[2])
        result = solution.addTwoNumbers(l1_test, l2_test)
        print(lists_are_equal(result, expect))
        i1 = get_listnode_as_str(l1_test)
        i2 = get_listnode_as_str(l2_test)
        r = get_listnode_as_str(result)
        e = get_listnode_as_str(expect)
        print(f"{i1=}\n{i2=}")
        print(f"{r=}\n{e=}\n")
