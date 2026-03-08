from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = deque([])
        carry = 0

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            val_a = int(a[i]) if i >= 0 else 0
            val_b = int(a[j]) if j >= 0 else 0

            total = val_a + val_b + carry

            carry = total // 2

            res.appendleft(str(total % 2))

            i -= 1
            j -= 1

        return "".join(res)
