class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        const long long MOD = 1000000007LL;
        int n = points.size();
        if (n < 4) return 0; // need at least 4 points to form a trapezoid

        // Count points per y-coordinate
        unordered_map<int,int> freq;
        for (auto &p : points) {
            freq[p[1]]++;
        }

        // For each y-level compute c = C(k,2) (number of distinct pairs on that line)
        vector<long long> combs;
        combs.reserve(freq.size());
        for (auto &kv : freq) {
            long long k = kv.second;
            if (k >= 2) combs.push_back( (k * (k-1) / 2) % MOD );
        }

        if (combs.size() < 2) return 0; // need at least two lines with >=2 points

        // Use formula: sum_{i<j} combs[i]*combs[j] = (S^2 - sumsq)/2
        long long S = 0, sumsq = 0;
        for (auto c : combs) {
            S = (S + c) % MOD;
            sumsq = (sumsq + (c * c) % MOD) % MOD;
        }

        long long ans = ( ( (S * S) % MOD - sumsq ) % MOD + MOD ) % MOD; // ensure non-negative
        // divide by 2 modulo MOD (MOD is prime), multiply by inverse of 2
        long long inv2 = (MOD + 1) / 2; // since MOD is 1e9+7, inverse of 2 is (MOD+1)/2
        ans = (ans * inv2) % MOD;
        return (int)ans;
    }
};
