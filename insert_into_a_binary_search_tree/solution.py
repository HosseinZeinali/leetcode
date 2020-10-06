class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if root == None:
            return TreeNode(val)
        current_node = root
        while True:
            if val > current_node.val:
                if current_node.right == None:
                    current_node.right = TreeNode(val)
                    break
                current_node = current_node.right
            else:
                if current_node.left == None:
                    current_node.left = TreeNode(val)
                    break
                current_node = current_node.left
        return root

    def makeTree(self):
        # root = TreeNode(10)
        # node5 = TreeNode(5)
        # nodem3 = TreeNode(-3)
        # node3 = TreeNode(3)
        # node2 = TreeNode(2)
        # node11 = TreeNode(11)
        # node3p = TreeNode(3)
        # nodem2 = TreeNode(-2)
        # node1 = TreeNode(1)
        # root.left = node5
        # root.right = nodem3
        # node5.left = node3
        # node5.right = node2
        # node3.left = node3p
        # node3.right = nodem2
        # node2.right = node1
        # nodem3.right = node11
        root = TreeNode(1)
        node1 = TreeNode(0)
        node1p = TreeNode(2)
        root.left = node1
        root.right = node1p

        return root
solution = Solution()
tree = solution.makeTree()
solution.insertIntoBST(tree, 5)