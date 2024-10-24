class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def subj(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            
            if root1.val!=root2.val:
                return False
            
            bool1 = subj(root1.left,root2.left) or subj(root1.left,root2.right)
            bool2 = subj(root1.right,root2.left) or subj(root1.right,root2.right)
            return bool1 and bool2
        
        return subj(root1,root2)