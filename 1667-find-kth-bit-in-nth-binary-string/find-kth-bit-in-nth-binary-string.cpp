class Solution {
public:
    string nstr(string curr){
        string temp = "";
        for (int i=curr.size()-1;i>=0;i--){
            if (curr[i]=='0'){
                temp+='1';
            }
            else{
                temp+='0';
            }
        }
        return curr+'1'+temp;
    }
    char findKthBit(int n, int k) {
        string ans = "0";
        while (n>0){
            ans = nstr(ans);
            n-=1;
        }   
        return ans[k-1];
    }
};