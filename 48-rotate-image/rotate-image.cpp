class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for(int j=0;j<n/2;j++){
            for(int i=0+j;i<n-1-j;i++){
                int temp = matrix[0+j][i];
                matrix[0+j][i]=matrix[n-i-1][0+j];
                matrix[n-i-1][0+j]=matrix[n-1-j][n-i-1];
                matrix[n-1-j][n-i-1]=matrix[i][n-1-j];
                matrix[i][n-1-j]=temp;
            }
        }
    }
};