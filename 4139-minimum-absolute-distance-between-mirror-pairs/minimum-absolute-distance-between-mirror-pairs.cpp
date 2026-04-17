class Solution {
public:
    int minMirrorPairDistance(vector<int>& nums) {
        map<int,vector<int>> mp;
        for(int i=0;i<nums.size();i++){
            mp[nums[i]].push_back(i);
            int rev = 0;
            int num = nums[i];
            while(num>0){
                rev = rev*10 + num%10;
                num/=10;
            }
            nums[i]=rev;
        }
        int ans =  INT_MAX;
        for(int i=0;i<nums.size();i++){
            if (mp.count(nums[i])){
                vector<int> &v = mp[nums[i]];
                if (v.size()==1 && i<v[0]) ans = min(ans,abs(i-v[0]));
                else if (v.size()==1){continue;}
                else{
                    for(int j=0;j<v.size();j++){
                        if(v[j]<=i) continue;
                        ans = min(ans,abs(i-v[j]));
                    }
                }
                if (ans == 1) return 1;
            }
        }
        if (ans == INT_MAX) return -1;
        return ans;
    }
};