
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def childNodes(self, i):
        return (2*i)+1, (2*i)+2

    def buildTree(self, array, i):
        if i >= len(array):
            return None
        t = TreeNode(array[i])
        lc, rc = self.childNodes(i)
        t.left = self.buildTree(array, lc)
        t.right = self.buildTree(array, rc)
        return t


s = Solution()
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]
x = s.buildTree(a, 0)
print(x)
