class Solution {
public:
    int maxDistance(vector<int>& colors) {
        int ans = 0;
        map<int,vector<int>> mp;
        for(int i=0;i<colors.size();i++){
            mp[colors[i]].push_back(i);
        }
        for(auto it1:mp){
            int e = it1.second.back();
            for(auto it2:mp){
                if(it1.first==it2.first) continue;
                int s = it2.second.front();
                ans = max(ans,abs(e-s));
            }
        }                                                                                  
        return ans;
    }
};