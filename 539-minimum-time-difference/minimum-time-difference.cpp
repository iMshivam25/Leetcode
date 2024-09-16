class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> temp;
        for (const auto &time : timePoints){
            int hour = stoi(time.substr(0,2));
            int minute = stoi(time.substr(3,2));
            temp.push_back(hour*60 + minute);
        }
        sort(temp.begin(),temp.end());
        int min_diff = INT_MAX;
        for(int i=1;i<temp.size();i++){
            int diff = abs(temp[i]-temp[i-1]);
            min_diff = min(min_diff,diff);
        }
        int circular_diff = 24*60 - temp.back() + temp[0];
        min_diff = min(min_diff, circular_diff);
        return min_diff;
    }
};