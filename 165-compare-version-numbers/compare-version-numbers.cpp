class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<int> split1;
        vector<int> split2;
        stringstream ss1(version1);
        stringstream ss2(version2);
        char delimiter = '.';
        string temp;
        while(getline(ss1,temp,delimiter)){
            const char* c1 = temp.c_str();
            for (int i=0;i<temp.length();i++){
                if (c1[i]!='0'){
                    temp = temp.substr(i);
                    int x = stoi(temp);
                    split1.push_back(x);
                    break;
                }
                if (i==temp.length()-1){split1.push_back(0);}
            }
        }
        while(getline(ss2,temp,delimiter)){
            const char* c2 = temp.c_str();
            for (int i=0;i<temp.length();i++){
                if (c2[i]!='0'){
                    temp = temp.substr(i);
                    int x = stoi(temp);
                    split2.push_back(x);
                    break;
                }
                if (i==temp.length()-1){split2.push_back(0);}
            }
            
        }
        int n = max(split1.size(),split2.size());
        int m = min(split1.size(),split2.size());
        for (int i=0;i<n;i++){
            if (i==m){
                if (split1.size()==n){
                    while(i!=n){
                        if (split1[i]!=0){
                            return 1;
                        }
                        i++;
                    }
                }
                else{
                    while(i!=n){
                        if (split2[i]!=0){
                            return -1;
                        }
                        i++;
                    }
                }
                break;
            }
            if (split1[i]>split2[i]){
                return 1;
            }
            else if (split1[i]<split2[i]){
                return -1;
            }
        }
        return 0;
    }
};