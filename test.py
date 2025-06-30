from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()

        # 遍历 nums，每次更新窗口和结果
        for i in range(len(nums)):
            print("---------------{}-------------".format(i))
            # 移除队首不在窗口范围内的元素（i - k）
            if window and window[0] <= i - k:
                print("1--", window)
                window.popleft()

            # 从队尾移除所有比当前 nums[i] 小的元素
            while window and nums[window[-1]] < nums[i]:
                print("2----nums[window[-1]]", nums[window[-1]])
                print("2-----nums[i]", nums[i])
                window.pop()
                print("2----window", window)

            # 将当前索引 i 加入队尾
            window.append(i)
            print("33333----window", window)

            # 当 i >= k - 1 时，把队首的 nums[索引] 加入 result
            if i >= k - 1:
                result.append(nums[window[0]])
                print("4-----window", window)
                print("4-----result", result)
        print("last----result",result)
        return result

s = Solution()
s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
s.maxSlidingWindow(nums = [1], k = 1)