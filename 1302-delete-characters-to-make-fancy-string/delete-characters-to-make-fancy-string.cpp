class Solution {
public:
    string makeFancyString(string s) {
        stringstream ss;
        char prev = '-';
        int count = 0;
        for (char ch:s){
            if (ch == prev) count++;
            else {
                prev=ch;
                count=1;
            }
            if (count<3){
                ss<<ch;
            }
        }
    return ss.str();
    }
};