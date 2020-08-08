# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        res = []
        self.helper(root,sum, [], res)

        return res
    def helper(self, root: TreeNode, sum, numsArray: [], res: []):
        numsArray.append(root.val)
        i = len(numsArray) - 1
        s = 0
        sumArray = []
        while i >= 0:
            s+= numsArray[i]
            if (s > sum):
                break
            sumArray.append(numsArray[i])
            if (s == sum):
                res.append(list(reversed(sumArray)))

            i = i -1
        if root.left != None:
            self.helper(root.left, sum, numsArray.copy(), res)
        if root.right != None:
            self.helper(root.right, sum, numsArray.copy(), res)
        return res


    def makeTree(self):
        root = TreeNode(10)
        node5 = TreeNode(5)
        nodem3 = TreeNode(-3)
        node3 = TreeNode(3)
        node2 = TreeNode(2)
        node11 = TreeNode(11)
        node3p = TreeNode(3)
        nodem2 = TreeNode(-2)
        node1 = TreeNode(1)
        root.left = node5
        root.right = nodem3
        node5.left = node3
        node5.right = node2
        node3.left = node3p
        node3.right = nodem2
        node2.right = node1
        nodem3.right = node11

        return root

solution = Solution()
root = solution.makeTree()
a = solution.pathSum(root, 8)
print(a)