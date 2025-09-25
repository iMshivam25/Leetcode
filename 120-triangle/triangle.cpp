class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int row = triangle.size();
        for (int i=1;i<row;i++){
            int col = triangle[i].size();
            for (int j=0;j<col;j++){
                if (j==0) triangle[i][j] += triangle[i-1][j];
                else if (j==col-1) triangle[i][j] += triangle[i-1][j-1];
                else {triangle[i][j] = triangle[i][j] + min(triangle[i-1][j],triangle[i-1][j-1]) ;}
                cout<<triangle[i][j]<<" ";
            }
        }
        int ans = INT_MAX;
        for (int i=0;i<triangle[row-1].size();i++){
            if (triangle[row-1][i]<ans) ans = triangle[row-1][i];
        }
    return ans;
    }
};