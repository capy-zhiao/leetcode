from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)
        print(nums)

        for i in range(length - 2):
            # 去重：跳过重复的 i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1

            print("i = %d, left = %d, right = %d" % (i, left, right))

            while left < right:
                print("nums[i] = %d, nums[left] = %d, nums[right] = %d" % (nums[i], nums[left], nums[right]))
                sum_all = nums[i] + nums[left] + nums[right]
                print("sum_all = %d" % sum_all)
                if sum_all > 0:
                    right -= 1
                    print("sum_all > 0, left = %d, right = %d" % (left, right))
                    continue
                elif sum_all < 0 :
                    left += 1
                    print("sum_all < 0, left = %d, right = %d" % (left, right))
                    continue
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    result.append(triplet)
                    print(triplet)
                    print(result)
                    right -= 1
                    left += 1
                    break
                    # # 找到一个三元组
                    # result.append([nums[i], nums[left], nums[right]])
                    # print(result)
                    # # 跳过重复的 left 元素
                    # while left < right and nums[left] == nums[left + 1]:
                    #     left += 1
                    #     print("left < right, left = %d, right = %d" % (left, right))
                    #     print("nums[left] = %d" % nums[left])
                    #     print("nums[left + 1] = %d" % nums[left + 1])
                    # # 跳过重复的 right 元素
                    # while left < right and nums[right] == nums[right - 1]:
                    #     right -= 1
                    #     print("right < left, right = %d, left = %d, right = %d" % (right, left, right))
                    #     print("nums[right] = %d" % nums[right])
                    #     print("nums[right - 1] = %d" % nums[right - 1])
                    # # 移动指针继续查找
                    # left += 1
                    # right -= 1
                    # print("left = %d" % left)
                    # print("right = %d" % right)

        return result

my = Solution()
print(my.threeSum([0, 0, 0, 0]))