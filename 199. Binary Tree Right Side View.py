from collections import deque
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right =  TreeNode(5)
root.right.right = TreeNode(4)

# Method 1 (DFS)
# Method 1

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        q = deque([root])
        result = []
        while q:
            n = len(q)
            temp = []
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(node.val)
            result.append(temp[-1])
        return result
                

print(BFS(root))

# Result:
#  Time Complexity O(N)
#  Space Complexity O(N)


# Method 2: (Using DFS)
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(root, level, result):
            if root == None:
                return
            if level + 1 > len(result):
                result.append(0)
            result[level] = root.val
            dfs(root.left, level + 1, result)
            dfs(root.right, level + 1, result)
        
        dfs(root, 0, result)
        return(result)
# Time Complexity : O(n)
# Space Complexity : o(log n)