class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> g;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                g.push_back(grid[i][j]);
            }
        }
        sort(g.begin(),g.end());
        int wrt = g[g.size()/2];
        int ans=0;
        for(int i=0;i<g.size();i++){
            if((g[i] - g[0]) % x != 0) return -1;
            ans+=abs(g[i]-wrt)/x;
        }
        return ans;
    }
};