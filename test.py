from collections import deque
from typing import List


class Solution:
    def reverse(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        print(chars)

    def reverseWords(self, s: str) -> str:
        result = list(s.strip())
        print(result)

        self.reverse(result, 0, len(result)-1)

        n = len(result)
        start = 0
        for end in range(n + 1):
            if end == n or result[end] == ' ':
                self.reverse(result, start, end - 1)
                start = end + 1

        return result
s = Solution()
s.reverseWords(s = "  hello world  ")