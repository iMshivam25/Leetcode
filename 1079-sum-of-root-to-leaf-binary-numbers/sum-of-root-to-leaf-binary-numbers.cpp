class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        if (!root) return 0;

        int total_sum = 0;

        // pair<node, current_binary_value>
        stack<pair<TreeNode*, int>> st;
        st.push({root, 0});

        while (!st.empty()) {
            auto [curr, value] = st.top();
            st.pop();

            // Build binary number so far
            value = (value << 1) | curr->val;

            // If it's a leaf
            if (!curr->left && !curr->right) {
                total_sum += value;
            }

            if (curr->right) {
                st.push({curr->right, value});
            }

            if (curr->left) {
                st.push({curr->left, value});
            }
        }

        return total_sum;
    }
};