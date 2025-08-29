# 动态规划基础

例如：有N件物品和一个最多能背重量为W 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。**每件物品只能用一次**，求解将哪些物品装入背包里物品价值总和最大。

动态规划中dp[j]是由dp[j-weight[i]]推导出来的，然后取max(dp[j], dp[j - weight[i]] + value[i])。

但如果是贪心呢，每次拿物品选一个最大的或者最小的就完事了，和上一个状态没有关系。

1. 确定dp数组（dp table）以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组

## 507 [Perfect Number](https://leetcode.com/problems/perfect-number/)

If i is the factor of num, then num/i is also a factor
Just traverse to √num and find a pair of factors each time

![image-20250829170906082](assets/image-20250829170906082.png)



## 70



## 746



## 62



## 63



## 343



## 96



# 背包问题





# 打家劫舍



# 股票



#  子序列

