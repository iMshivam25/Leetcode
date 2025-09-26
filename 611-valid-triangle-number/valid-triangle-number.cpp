class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int ans=0;
        for(int i=0;i<n;i++){
            vector<int> temp;
            for(int j=i+1;j<n;j++){
                if (temp.size()==0) {}
                else{
                    int k=temp.size();
                    if (temp[k/2]<nums[i]){
                        ans+=k/2;
                        k=k/2;
                    }
                    else{
                        k=temp.size()-1;
                    }
                    for (k;k>=0;k--){  
                        
                        if (nums[j]<temp[k]){
                            ans++;
                        }
                        else break;
                    }
                }                         
                temp.push_back(nums[i]+nums[j]);
            }
        }
        return ans;
    }
};         