# 前提

## 完全二叉树

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层（h从1开始），则该层包含 1~ 2^(h-1) 个节点。

<img src="assets/68747470733a2f2f66696c65312e6b616d61636f6465722e636f6d2f692f616c676f2f32303230303932303232313633383930332e706e67.png" alt="img" style="width:50%;" />

## 二叉搜索树

前面介绍的树，都没有数值的，而二叉搜索树是有数值的了，**二叉搜索树是一个有序树**。

- 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
- 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
- 它的左、右子树也分别为二叉排序树

下面这两棵树都是搜索树

[<img src="assets/68747470733a2f2f66696c65312e6b616d61636f6465722e636f6d2f692f616c676f2f32303230303830363139303330343639332e706e67.png" alt="img" style="width:50%;" />](https://camo.githubusercontent.com/8539fe8e5f70e95820fce7dc0abf9f1705b03fa19f3f152d881847952a1e9c1b/68747470733a2f2f66696c65312e6b616d61636f6465722e636f6d2f692f616c676f2f32303230303830363139303330343639332e706e67)

## 平衡二叉搜索树

平衡二叉搜索树：又被称为AVL（Adelson-Velsky and Landis）树，且具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。

如图：

[<img src="assets/68747470733a2f2f66696c65312e6b616d61636f6465722e636f6d2f692f616c676f2f32303230303830363139303531313936372e706e67.png" alt="img" style="width:50%;" />](https://camo.githubusercontent.com/d55d08174281c5a4e6aa6ac13de38c7394c289bea3d5012d2c847cc096c5efea/68747470733a2f2f66696c65312e6b616d61636f6465722e636f6d2f692f616c676f2f32303230303830363139303531313936372e706e67)

最后一棵 不是平衡二叉树，因为它的左右两个子树的高度差的绝对值超过了1。

## 遍历方式

- 前序遍历：中左右
- 中序遍历：左中右
- 后序遍历：左右中

<img src="assets/68747470733a2f2f66696c65312e6b616d61636f6465722e636f6d2f692f616c676f2f32303230303830363139313130393839362e706e67.png" alt="img" style="width:50%;" />

# 题目

## 遍历

### easy 144 [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

buyong递归

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            print(node.val)
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
```

### easy 145 [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

no 递归

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        return res[::-1]
```

### med 95[Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)

对于区间 `[start, end]`，尝试每个 `i` 作为根节点；

递归生成所有 `i` 左边的树（作为左子树）；

递归生成所有 `i` 右边的树（作为右子树）；

每个 `左子树 × 右子树` 的组合，和根节点组合成一棵树。

```python
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def build(start, end):
            if start > end:
                return [None]
            
            trees = []
            for i in range(start, end + 1):
                left = build(start, i - 1)
                right = build(i + 1, end)
                for l in left:
                    for r in right:
                        trees.append(TreeNode(i, l, r))

            return trees

        return build(1, n)
```

### med 102 [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

**初始化一个队列**，将根节点放入；

**循环处理队列**直到为空：

- 当前层有多少个节点就处理多少次；
- 依次弹出这些节点，加入结果；
- 将它们的左右孩子（如果有）加入队列；

最终返回按层分组的结果。

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_nodes = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node .right:
                    queue.append(node.right)
            res.append(level_nodes)
                
        return res

```

## 属性

### easy [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

要比较两个节点数值相不相同，首先要把两个节点为空的情况弄清楚！否则后面比较数值的时候就会操作空指针了。

节点为空的情况有：（**注意我们比较的其实不是左孩子和右孩子，所以如下我称之为左节点右节点**）

- 左节点为空，右节点不为空，不对称，return false
- 左不为空，右为空，不对称 return false
- 左右都为空，对称，返回true

此时已经排除掉了节点为空的情况，那么剩下的就是左右节点不为空：

- 左右都不为空，比较节点数值，不相同就return false

此时才进入单层递归的逻辑，单层递归的逻辑就是处理 左右节点都不为空，且数值相同的情况。

- 比较二叉树外侧是否对称：传入的是左节点的左孩子，右节点的右孩子。
- 比较内侧是否对称，传入左节点的右孩子，右节点的左孩子。
- 如果左右都对称就返回true ，有一侧不对称就返回false 。

递归

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Compare(self, left, right):
        
        if(left == None and right != None): return False
        if(left != None and right == None): return False
        if(left == None and right == None): return True
        print(left.val, right.val)
        if (left.val != right.val): return False

        outside = self.Compare(left.left, right.right)
        inside = self.Compare(left.right, right.left)
        issame = outside & inside
        return issame

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.Compare(root.left, root.right)
```

迭代

这个迭代法，其实是把左右两个子树要比较的元素顺序放进一个容器，然后成对成对的取出来进行比较

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        stack.append(root.right)
        stack.append(root.left)
        
        while stack:
            left = stack.pop()
            right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False

            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True
```



### 104 [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

本题可以使用前序（中左右），也可以使用后序遍历（左右中），使用前序求的就是深度，使用后序求的是高度。

- 二叉树节点的深度：指从根节点到该节点的最长简单路径边的条数或者节点数（取决于深度从0开始还是从1开始）
- 二叉树节点的高度：指从该节点到叶子节点的最长简单路径边的条数或者节点数（取决于高度从0开始还是从1开始）

**而根节点的高度就是二叉树的最大深度**，所以本题中我们通过后序求的根节点高度来求的二叉树最大深度。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def godeep(self, node, count):
        if node == None:
            return count
        count += 1
        leftdeep = self.godeep(node.left, count)
        rightdeep = self.godeep(node.right, count)
        return max(leftdeep, rightdeep)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None : return 0
        count = 0
        return self.godeep(root, count)
```

### 111 [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

如果左子树为空，右子树不为空，说明最小深度是 1 + 右子树的深度。

反之，右子树为空，左子树不为空，最小深度是 1 + 左子树的深度。

最后如果左右子树都不为空，返回左右子树深度最小值 + 1 

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def godeep(self, node, count):
        if not node.left and not node.right:
            return count

        if not node.left and node.right:
            return self.godeep(node.right, count+1)
        if not node.right and node.left:
            return self.godeep(node.left, count+1)
        
        left_depth = self.godeep(node.left, count + 1)
        right_depth = self.godeep(node.right, count + 1)

        return min(left_depth, right_depth)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count = 1
        return self.godeep(root, count)
        
```

### 222[Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        count = 0
        queue = deque()
        queue.append(root)
        
        while queue:

            node = queue.popleft()
            count += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return count
            
```

### 110 [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def godeep(self, node, count):
        if node is None:
            return count
        count += 1
        leftdepth = self.godeep(node.left, count)
        rightdepth = self.godeep(node.right, count)
        return max(leftdepth, rightdepth)
    


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        count = 1
        if root.left:
            lc = self.godeep(root.left, count)
        else:
            lc = 1
        if root.right:
            rc = self.godeep(root.right, count)
        else:
            rc = 1
        if abs(lc - rc) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
```

### 257[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

这道题目要求从根节点到叶子的路径，所以需要前序遍历，这样才方便让父节点指向孩子节点，找到对应的路径。

在这道题目中将第一次涉及到回溯，因为我们要把路径记录下来，需要回溯来回退一个路径再进入另一个路径。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result = []

        def dfs(node, path):
            if not node: return 
            path += str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                path+="->"
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return result
```

### 404[Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)

我们可以用**深度优先遍历（DFS）**来解决，整体思路如下：

1. **遍历整棵树**，每到一个节点，就检查它的左孩子。
2. 如果左孩子存在，**且是叶子节点（没有左、右子节点）**，就把它的值加入总和中。
3. 不管左孩子是不是叶子，都要**继续递归地向左右子树遍历**，直到遍历完整棵树。
4. 最后返回累加的结果。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            nonlocal result
            if not node:
                return 
            if node.left and not node.left.right and not node.left.left:
                print(result)
                result += node.left.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result
```

### 513[Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/)

可以用 **DFS** 递归遍历整棵树，同时追踪两个信息：

1. 当前递归到的深度（`depth`）
2. 当前发现的最深层级（`max_depth`），以及该层的最左值（`left_value`）

------

#### 🔍 DFS 实现核心逻辑：

- 从根节点开始递归，起始深度为 0。
- 每深入一层，深度加 1。
- 每次访问**第一个到达的新深度**的节点时，记录它的值（因为 DFS 是先访问左子树，所以这个值就是最左边的）。
- 用两个变量持续更新：`max_depth` 和 `left_value`

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = -1
        left_value = 0

        def dfs(node, depth):
            nonlocal max_depth, left_value

            if not node:
                return 
            if depth > max_depth:
                max_depth = depth
                left_value = node.val 


            dfs(node.left, depth +1)
            dfs(node.right, depth +1)

        dfs(root, 0)
        return left_value
```

### 112[Path Sum](https://leetcode.com/problems/path-sum/)



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        result = []

        def dfs(node, sumall):
            if not node:
                return
            sumall += node.val
            if not node.left and not node.right:
                result.append(sumall)
            
            dfs(node.left, sumall)
            dfs(node.right, sumall)

        dfs(root, 0)

        return targetSum in result
```

## 修改与构造

### 226[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)




```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return 
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
```
### 106[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

Inorder:中序遍历,左根右 9 3 15 20 7

Postorder:左右根9 15 7 20 3

**后序遍历的最后一个元素是根节点。**

**中序遍历中，根节点左边的是左子树，右边的是右子树。**


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)
        print(root_val)

        root_index = inorder.index(root_val)

        left_in = inorder[:root_index]
        # print(left_in)
        right_in = inorder[root_index+1:]
        # print(right_in)

        left_post = postorder[:len(left_in)]
        # print(left_post)
        right_post = postorder[len(left_in):-1]
        # print(right_post)



        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)
        return root
```
### 105



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        index = inorder.index(root_val)
        
        leftin = inorder[:index]
        rightin = inorder[index+1:]

        leftpre = preorder[1:len(leftin)+1]
        rightpre = preorder[len(leftin)+1:]

        root.left = self.buildTree(leftpre, leftin)
        root.right = self.buildTree(rightpre, rightin)
        
        return root
```



### 654[Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/)




```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 
        max_num = max(nums)
        max_index = nums.index(max_num)
        root = TreeNode(max_num)

        lefttree = nums[:max_index]
        righttree = nums[max_index+1:]

        root.left = self.constructMaximumBinaryTree(lefttree)
        root.right = self.constructMaximumBinaryTree(righttree)

        return root
```
### 617[Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2: return root2
        if root2 is None and root1: return root1
        if root1 is None and root2 is None: return

        new_t = TreeNode(root1.val+root2.val)
        new_t.left = self.mergeTrees(root1.left, root2.left)
        new_t.right = self.mergeTrees(root1.right, root2.right)

        return new_t
```

## 属性

### 700[Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None: return

        print("-------{}------".format(root.val))
        
        
        if(root.val == val):
            print("==", root.val)
            return root
        elif(val < root.val):
            print("<")
            return self.searchBST(root.left, val)
        elif(val > root.val):
            print(">")
            return self.searchBST(root.right, val)
```

### 98[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)



```python
class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def vali(left, node, right):
            if not node: return True
            if not(left < node.val < right): return False
            return vali(left, node.left, node.val) and vali(node.val, node.right, right)

        return vali(float('-inf'), root, float('inf'))

```

### 530[Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_diff = float('inf')
        def inorder(node):
            nonlocal prev, min_diff
            if not node: return
            inorder(node.left)

            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))
            prev = node.val

            inorder(node.right)

        inorder(root)
        return min_diff
```

### 501[Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

对整棵树进行 **中序遍历**（BST 中序是递增的）

使用一个字典或计数器记录每个值出现的次数

找出最大频率，把所有出现这个频率的值返回

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        freq = defaultdict(int)

        def inorder(root):
            nonlocal freq
            if root.left:
                inorder(root.left)
            freq[root.val] += 1
            if root.right:
                inorder(root.right)
        inorder(root)
        max_count = max(freq.values())
        return [val for val, count in freq.items() if count == max_count]
```

### 538[Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def dfs(node):
            nonlocal total
            if not node: return 

            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)

        dfs(root)
        return root
```

## 公共祖先:

### 236[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

#### 1. 递归遍历（DFS）：

- 利用递归函数从根节点开始向下搜索。
- 思考：当前节点是否是 `p` 或 `q`？是否在其左右子树中能找到另一个节点？

#### 2. 三种情况：

- 如果在**左子树**找到一个节点，在**右子树**找到另一个节点，那么当前节点就是 LCA。
- 如果在当前子树中只找到一个节点，另一个节点不在这棵子树中，那么往上传递这个已找到的节点。
- 如果当前节点就是 `p` 或 `q`，也应该作为结果的一部分向上传递。

#### 3. 递归终止条件：

- 当前节点为空，返回 `None`。
- 当前节点等于 `p` 或 `q`，直接返回当前节点。

#### 4. 回溯的核心：

- 从下往上逐步判断左右子树是否包含目标节点，根据返回结果来判断谁是 LCA。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None: return None

            if (node == p or node == q): return node

            leftn = dfs(node.left)
            rightn = dfs(node.right)

            if leftn and rightn: return node

            if not leftn: return rightn
            elif not rightn: return leftn 
        return dfs(root)
```

### 235[Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

#### 核心逻辑：**利用 BST 的大小关系来走路！**

给你两个节点 `p` 和 `q`，你从根节点开始判断：

#### ✅ 情况一：

如果：

```
p.val < root.val  且  q.val < root.val
```

说明 `p` 和 `q` 都在当前节点的**左子树**里 —— 递归或迭代往左走。

#### ✅ 情况二：

如果：

```
p.val > root.val  且  q.val > root.val
```

说明 `p` 和 `q` 都在当前节点的**右子树**里 —— 往右走。

#### ✅ 情况三（最重要）：

如果：

```
一个在左，一个在右，或者当前节点就是其中一个
```

那么当前节点就是最近公共祖先（LCA）。

因为这是它们路径**第一次分叉的地方**，或者说是“共同路过的最低点”。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return None
            if(p.val>node.val and q.val<node.val): 
                return node
            if(p.val<node.val and q.val>node.val): 
                return node
            if p.val == node.val or q.val == node.val: 
                return node

            if(p.val < node.val and q.val < node.val): 
                return dfs(node.left)
            if(p.val > node.val and q.val > node.val): 
                return dfs(node.right)

        return dfs(root)
```



## 搜索树修改与构造

### 701[Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

#### 🌲 BST 的性质复习：

> 对于任意一个节点：

- 所有左子树的节点值都 **小于当前节点值**；
- 所有右子树的节点值都 **大于当前节点值**。

这个性质是我们插入的关键。

------

#### 🧠 解题思路：

#### 方法一：**递归插入（DFS）**

1. 从 `root` 开始比较：
   - 如果 `val < node.val`，往左子树递归；
   - 如果 `val > node.val`，往右子树递归；
2. 当你发现对应的左/右子节点是 `None`，就**把新节点插在这里**。

👉 因为题目保证新值在树中不存在，所以不需要考虑等于的情况。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if node is None: 
                return TreeNode(val)
            if node.val > val: node.left = dfs(node.left)
            if node.val < val: node.right = dfs(node.right)
            return node

        return dfs(root)

```

### 450[ Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

- 第一种情况：没找到删除的节点，遍历到空节点直接返回了
- 找到删除的节点
  - 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
  - 第三种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
  - 第四种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
  - 第五种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root

        if root.val == key:
            if not root.right:
                return root.left
            
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val, cur.val = cur.val, root.val

        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)

        return root
            
```

### 669[Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
```

### 108[Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        middle = TreeNode(nums[mid])
        middle.left = self.sortedArrayToBST(nums[:mid])
        middle.right = self.sortedArrayToBST(nums[mid+1:])
        return middle
```

