from collections import deque
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0]*n for i in range(n)]
        top = 0
        bottom = n-1
        left = 0
        right = n-1
        num =1
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                result[left][i] = num
                num += 1
                print("1------", num, left, right)
            top+=1

            for i in range(top, bottom+1):
                result[i][right] = num
                num += 1
                print("2------", num, left, right)
            right -= 1

            for i in range(right, left-1, -1):
                result[bottom][i] = num
                num+=1
                print("3------", num, left, right)
            bottom -= 1

            for i in range(bottom, top-1, -1):
                result[i][left] = num
                num+=1
                print("4------", num, left, right)
            left += 1
        print(result)
        return result
S = Solution()
S.generateMatrix(4)
