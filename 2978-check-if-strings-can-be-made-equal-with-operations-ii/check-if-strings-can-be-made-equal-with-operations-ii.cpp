class Solution {
public:
    bool checkStrings(string s1, string s2) {
        if (s1.size()!=s2.size()) return false;
        bool ans=true;
        int s = s1.size();
        for(int i=0;i<s;i++){
            if(s1[i]==s2[i]) continue;
            bool flag = false;
            for(int j=i+2;j<s;j=j+2){
                if(s1[j]==s2[i]){
                    char temp = s1[i];
                    s1[i]=s1[j];
                    s1[j]=temp;
                    flag = true;
                    break;
                }
            }
            if (flag==false){
                ans = false;
                break;
            }
        }
        return ans;
    }
};