class Solution {
public:
    int numSub(string s) {
        long long int mod = 1000000007;
        long long sum = 0;
        long long count = 0;
        for (char ch : s){
            if (ch == '1') count++;
            else{
                sum += ((count*(count+1))/2);
                sum %= mod;
                count = 0;
            }
        }
        if (count>0){
            sum += ((count*(count+1))/2);
            sum %= mod;
        }
    return sum;
    }
};