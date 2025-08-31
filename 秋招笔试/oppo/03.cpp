#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];

        unordered_map<int,int> first,last;
        for (int i = 0; i < n; i++) {
            int v = arr[i];
            if (!first.count(v)) first[v] = i;
            last[v] = i;
        }

        vector<int> vals;
        vals.reserve(first.size());
        for (auto &p : first) vals.push_back(p.first);
        sort(vals.begin(), vals.end());

        int total = (int)vals.size();
        int best = 1, cur = 1;

        for (int i = 1; i < total; i++) {
            int v = vals[i], u = vals[i-1];
            if (v == u + 1 && last[u] < first[v]) {
                cur++;
            } else {
                cur = 1;
            }
            best = max(best, cur);
        }

        int ans = total - best;
        cout << ans << "\n";
    }
    return 0;
}
