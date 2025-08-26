#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	if (!(cin >> T)) return 0;
	while (T--) {
		int n; cin >> n;
		vector<vector<long long>> a(n, vector<long long>(n));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) cin >> a[i][j];
		}

		vector<vector<long long>> prefix(n, vector<long long>(n + 1, 0));
		vector<long long> row_sum(n, 0);
		for (int i = 0; i < n; ++i) {
			long long ps = 0;
			for (int j = 0; j < n; ++j) {
				ps += a[i][j];
				prefix[i][j + 1] = ps;
			}
			row_sum[i] = ps;
		}

		long long ans = 0;
		for (int c = 1; c <= n; ++c) {
			long long base = prefix[0][c - 1];
			for (int i = 0; i < n; ++i) {
				long long tail;
				if ((i + 1) % 2 == 1) {
					// odd row, moving right: collect c..n
					tail = row_sum[i] - prefix[i][c - 1];
				} else {
					// even row, moving left: collect 1..c
					tail = prefix[i][c];
				}
				ans = max(ans, base + tail);
			}
		}

		cout << ans << '\n';
	}
	return 0;
}


