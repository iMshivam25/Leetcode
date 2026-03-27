class Solution {
public:
    bool areSimilar(vector<vector<int>>& mat, int k) {
        // bool ans;
        int m=mat.size();
        int n=mat[0].size();
        k=k%n;
        vector<vector<int>> temp(m, vector<int>(n,0));
        for(int i=0;i<m;i++){
            if (i%2==0){
                for(int j=0;j<n;j++){
                    temp[i][j]=mat[i][(j+k)%n];
                }
                continue;
            }
            else{
                for(int j=0;j<n;j++){
                    temp[i][j]=mat[i][(j-k+n)%n];
                }
                continue;
            }
        }
        return temp==mat;
    }
};