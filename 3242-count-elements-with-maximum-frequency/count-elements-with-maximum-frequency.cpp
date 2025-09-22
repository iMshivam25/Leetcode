class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int,int> temp;
        int max=0;
        for (int i=0;i<nums.size();i++){
            temp[nums[i]]++;
            if (temp[nums[i]]>max) max=temp[nums[i]];
        }
        int count=0;
        for (auto it:temp){
            if (it.second==max) count++;
        }
    return count*max;
    }
};