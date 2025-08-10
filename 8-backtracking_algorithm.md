# intro

回溯法其实就是暴力查找

### 回溯法解决的问题

回溯法，一般可以解决如下几种问题：

- 组合问题：N个数里面按一定规则找出k个数的集合
- 切割问题：一个字符串按一定规则有几种切割方式
- 子集问题：一个N个数的集合里有多少符合条件的子集
- 排列问题：N个数按一定规则全排列，有几种排列方式
- 棋盘问题：N皇后，解数独等等

在上面我们提到了，回溯法一般是在集合中递归搜索，集合的大小构成了树的宽度，递归的深度构成的树的深度。

如图：

[![回溯算法理论基础](assets/68747470733a2f2f66696c65312e6b616d61636f6465722e636f6d2f692f616c676f2f32303231303133303137333633313137342e706e67.png)](https://camo.githubusercontent.com/328809c1183b5aa1d1a01628de89ce4e55f97328307746a8eb9b74db7a318d9b/68747470733a2f2f66696c65312e6b616d61636f6465722e636f6d2f692f616c676f2f32303231303133303137333633313137342e706e67)

注意图中，我特意举例集合大小和孩子的数量是相等的！

# 组合

## 77[Combinations](https://leetcode.com/problems/combinations/)

![image-20250722155927454](assets/image-20250722155927454.png)

## 17[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

![image-20250722161511420](assets/image-20250722161511420.png)

## 39[Combination Sum](https://leetcode.com/problems/combination-sum/)

![image-20250722173042432](assets/image-20250722173042432.png)

## 40[Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

![image-20250722235908520](assets/image-20250722235908520.png)

## 216[Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

![image-20250723000941850](assets/image-20250723000941850.png)

# 分割

## 131[Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

![image-20250723231648797](assets/image-20250723231648797.png)

## 93[Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

| 步骤     | 内容                           |
| -------- | ------------------------------ |
| 剪枝     | 长度不在 4~12 之间直接返回空   |
| 回溯     | 枚举每段 1~3 个字符            |
| 判断合法 | 每段不能大于 255，不能有前导零 |
| 终止条件 | 切满 4 段并且用完所有字符      |

![image-20250723234510798](assets/image-20250723234510798.png)

# 子集

## 78[Subsets](https://leetcode.com/problems/subsets/)

![image-20250726105125818](assets/image-20250726105125818.png)

## 90[Subsets II](https://leetcode.com/problems/subsets-ii/)

![image-20250726110520673](assets/image-20250726110520673.png)

# 排列

## 46[Permutations](https://leetcode.com/problems/permutations/)



## 47



# 棋盘

## 51



## 37



# remain

## 491



## 332

