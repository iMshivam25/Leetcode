class Solution {
public:
    int countBinarySubstrings(string s) {
        vector<int> temp;
        int c0=0, c1=0;
        bool is0 = (s[0]=='0') ? true : false;
        int ans=0;
        for(char ch:s){
            if (is0){
                if (ch=='0'){c0++;}
                else{
                    temp.push_back(c0);
                    c0=0;
                    c1=1;
                    is0 = false;
                }
            }
            else{
                if (ch=='1'){c1++;}
                else{
                    temp.push_back(c1);
                    c0=1;
                    c1=0;
                    is0 = true;
                }
            }
        }
        if (c0!=0){temp.push_back(c0);}
        else{temp.push_back(c1);}
        for(int i=0;i<temp.size()-1;i++){
            ans+=min(temp[i],temp[i+1]);
        }
        return ans;
    }
};