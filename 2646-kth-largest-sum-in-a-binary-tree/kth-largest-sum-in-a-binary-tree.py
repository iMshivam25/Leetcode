class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        slvl = []
        curr = [root]
        while curr:
            temp = 0
            next_lvl = []
            for node in curr:
                temp += node.val
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            slvl.append(temp)
            curr = next_lvl
        slvl = sorted(slvl, reverse = True)
        if len(slvl)<k:
            return -1
        return slvl[k-1]