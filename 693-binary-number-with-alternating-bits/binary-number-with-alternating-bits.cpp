class Solution {
public:
    bool hasAlternatingBits(int n) {
        bool ans = true;
        vector<int> bits;
        while(n>0){
            bits.push_back(n%2);
            n/=2;
        }
        int i=bits.size()-1;
        while(i>=1){
            cout<<bits[i];
            if (bits[i]^bits[i-1]==0){
                return false;
            }
            i--;
        }
        return ans;
    }
};