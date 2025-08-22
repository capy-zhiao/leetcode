# Greedy Algorithm

The only difficulty lies in how to derive the global optimum from local optima.
 A greedy algorithm is generally divided into the following four steps:

1. Decompose the problem into several subproblems
2. Identify an appropriate greedy strategy
3. Solve each subproblem optimally
4. Combine the local optimal solutions into a global optimal solution



## 455 [Assign Cookies](https://leetcode.com/problems/assign-cookies/)

![image-20250818143519118](assets/image-20250818143519118.png)



## 376[Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)

When the sign of `diff` is different from the previously recorded sign (from up → down or down → up), increase the count by 1 and update the "previous sign".

The initial length is at least 1; when the first non-zero difference appears, set the length to 2.

![image-20250819150921725](assets/image-20250819150921725.png)



## 53[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

keep two variables:

- `result`: the current running subarray sum
- `best`: the maximum subarray sum

For each number in `nums`:

1. Add it to `result`.
2. Update `best` if `result` is larger.
3. If `result` becomes negative, reset it to `0` (start a new subarray).

At the end, `best` is the answer.

![image-20250822165751471](assets/image-20250822165751471.png)



## 122[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

Easy to write if you know the principle.
 As long as `prices[i] > prices[i-1]`, add the difference `prices[i] - prices[i-1]` to the profit.

![image-20250819163415793](assets/image-20250819163415793.png)



## 55[Jump Game](https://leetcode.com/problems/jump-game/)

```python
nums = [2,3,1,1,4]`
Begin: `farthest = 0
```

- **i = 0**: you can jump to `0 + nums[0] = 2`, so update `farthest = 2`.
- **i = 1**: now `i = 1 <= farthest = 2`, so index 1 is reachable; from 1 you can jump to `1 + 3 = 4`, update `farthest = 4`.
- **i = 2**: now `i = 2 <= farthest = 4`, still reachable; from 2 you can only jump to 3, which is not farther than 4, so `farthest` stays the same.
- Finally, `farthest = 4 >= len(nums) - 1`, so the last index is reachable → return **true**.

![image-20250822171439726](assets/image-20250822171439726.png)



## 45[Jump Game II](https://leetcode.com/problems/jump-game-ii/)

Example (`[2,3,1,1,4]`):

- Initial: `steps = 0, end = 0, farthest = 0`
- **i = 0**: `farthest = max(0, 0+2) = 2`; since `i == end`, we make a jump → `steps = 1, end = 2`
- **i = 1**: `farthest = max(2, 1+3) = 4`
- **i = 2**: `farthest = max(4, 2+1) = 4`; since `i == end`, we make another jump → `steps = 2, end = 4`
- Done. Answer = **2**.

![image-20250822173836683](assets/image-20250822173836683.png)

## 1005[Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)

For the first part, we should sort the array and flip all negative numbers to positive.

For the second part, if there are still some operations left, then:

- if `k mod 2 is 0`, flipping has no influence on the result,
- otherwise, we should sort the array again and flip the element with the smallest absolute value.

![image-20250818144541953](assets/image-20250818144541953.png)



## 134



## 135





## 860[Lemonade Change](https://leetcode.com/problems/lemonade-change/)

use five and ten to solute

![image-20250818152431787](assets/image-20250818152431787.png)



## 406





## 452



## 435



## 763



## 56





## 738[Monotone Increasing Digits](https://leetcode.com/problems/monotone-increasing-digits/)

```python
Convert the integer to a string
Traverse the string from right to left
If the current character is smaller than the previous one, 
	it means we need to modify the previous character
Decrease the previous character by 1
Set all characters after the modified position to 9
Convert the list back to a string, then convert the string to an integer and return it
```

![image-20250819155943499](assets/image-20250819155943499.png)

## 

## 968





## 
