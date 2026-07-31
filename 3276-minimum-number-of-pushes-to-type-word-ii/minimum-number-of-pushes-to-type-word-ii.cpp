class Solution {
public:
    int minimumPushes(string word) {
        map<char,int> occ;
        for(char ch:word) occ[ch]++;
        vector<pair<char,int>> vec(occ.begin(),occ.end());
        sort(vec.begin(),vec.end(),[](const auto &a, const auto &b){return a.second>b.second;});
        int ans = 0;
        int ix=0;
        for(const auto &p : vec){
            int t = (ix/8)+1;
            ans+=(p.second*t);
            ix++;
        }
        return ans;
    }
};