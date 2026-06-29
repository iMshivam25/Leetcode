class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int ans = 0;
        int n = word.length();
        unordered_map<string,int> mp;
        mp[word]++;
        for(int i=1;i<n;i++){
            for(int j=0;i+j<=n;j++){
                string temp = word.substr(j,i);
                cout<<temp<<endl;
                mp[temp]++;
            }
        }
        int count=0;
        for(auto it:patterns)
        {
            if(mp.find(it)!=mp.end()) ans++;
        }

        return ans;
    }
};