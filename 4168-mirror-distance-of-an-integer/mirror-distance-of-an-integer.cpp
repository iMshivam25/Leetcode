class Solution {
public:
    int mirrorDistance(int n) {
        int rev=0;
        int m=n;
        while(m!=0){
            int digit = m%10;
            rev = rev*10 + digit;
            m/=10;
        }
        cout<<rev;
        return abs(rev-n);
    }
};