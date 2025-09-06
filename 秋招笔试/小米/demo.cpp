#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (!(cin >> T)) return 0;
    const long long INF = (long long)4e18;

    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<vector<long long>> a(n, vector<long long>(m));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> a[i][j];

        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, INF));
        dp[n][m - 1] = 1;
        dp[n - 1][m] = 1;

        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                long long need_next = min(dp[i + 1][j], dp[i][j + 1]);
                dp[i][j] = max(1LL, need_next - a[i][j]);
            }
        }
        cout << dp[0][0] << "\n";
    }
    return 0;
}