class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> ans;
        if (turnedOn >=9) return ans;
        vector<vector<string>> hour;
        hour.push_back({"0"});
        hour.push_back({"1","2","4","8"});
        hour.push_back({"3","5","6","9","10"});
        hour.push_back({"7","11"});
        vector<vector<string>> minutes;
        minutes.push_back({"00"});
        minutes.push_back({"01","02","04","08","16","32"});
        minutes.push_back({"03","05","09","17","33","06","10","18","34","12","20","36","24","40","48"});
        minutes.push_back({"07","11","13","14","19","21","22","25","26","28","35","37","38","41","42","44","49","50","52","56"});
        minutes.push_back({"15","23","27","29","30","39","43","45","46","51","53","54","57","58"});
        minutes.push_back({"31","47","55","59"});

        int mi = min(turnedOn,5);
        int hr = turnedOn - mi;
        while(hr<=3 && mi >=0){
            for(int i=0;i<hour[hr].size();i++){
                for(int j=0;j<minutes[mi].size();j++){
                    string temp = hour[hr][i] + ":" + minutes[mi][j];
                    ans.push_back(temp);
                }
            }
            hr++;
            mi--;
        }
        return ans;
    }
};