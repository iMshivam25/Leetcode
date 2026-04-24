class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        int count = 0;
        int ss = 0;
        for(char ch:moves){
            if (ch == 'L') count--;
            else if (ch == 'R') count++;
            else ss++;
        }
        return abs(count)+ss;
    }
};