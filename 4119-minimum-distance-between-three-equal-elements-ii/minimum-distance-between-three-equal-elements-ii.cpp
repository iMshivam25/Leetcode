class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        unordered_map<int, vector<int>> mp;

        for (int i = 0; i < nums.size(); i++) {
            mp[nums[i]].push_back(i);
        }

        int ans = INT_MAX;

        for (auto &it : mp) {
            vector<int> &temp = it.second;

            if (temp.size() >= 3) {
                for (int i = 0; i + 2 < temp.size(); i++) {
                    int a = temp[i];
                    int b = temp[i + 1];
                    int c = temp[i + 2];

                    int sum = abs(a - b) + abs(b - c) + abs(a - c);
                    ans = min(ans, sum);
                }
            }
        }

        return (ans == INT_MAX) ? -1 : ans;
    }
};
