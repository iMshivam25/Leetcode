class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        long long n = numerator;
        long long d = denominator;
        stringstream ss;
        if (n==0) return to_string(0);
        if (n<0 && d>0) {
            ss<<"-";
            n *= -1;
        }
        if (d<0 && n>0) {
            ss<<"-";
            d *= -1;
        }
        ss<<n/d;
        long long rem = n%d;
        if (rem==0){
            string ans = ss.str();
            return ans;    
        }
        ss<<'.';
        map<long long,int> seen;
        int i=0;
        string temp = "";
        bool flag = false;
        while (rem!=0){
            seen[rem]=i;
            i++;
            rem *= 10;
            temp+=to_string(rem/d);
            rem  = rem%d;
            if (seen.count(rem)){
                string t = temp.substr(0,seen[rem])+"("+temp.substr(seen[rem],temp.length())+")"; 
                ss<<t;
                flag = true;
                break;
            }
        }
        if (flag == false){
            ss<<temp;
        }
        string ans = ss.str();
        return ans;
    }
};