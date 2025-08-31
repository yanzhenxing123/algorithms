#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];

        int threshold = (n + 1) / 2;
        vector<int> freq(n + 1, 0);

        // 初始频率统计
        for (int v : arr) freq[v]++;
        int max_freq = *max_element(freq.begin(), freq.end());

        int ans = 0;
        if (max_freq >= threshold) ans++;

        for (int i = 0; i < m; i++) {
            int x, y;
            cin >> x >> y;
            x--; // 转成0-index
            int old = arr[x];
            int nw = y;

            if (old == nw) {
                if (max_freq >= threshold) ans++;
                continue;
            }

            // 更新频率
            freq[old]--;
            freq[nw]++;
            arr[x] = nw;

            // 更新 max_freq
            if (freq[nw] > max_freq) {
                max_freq = freq[nw];
            } else if (freq[old] + 1 == max_freq && freq[old] < max_freq) {
                // 如果原来是最大值且被减小了，需要重新扫描
                max_freq = *max_element(freq.begin(), freq.end());
            }

            if (max_freq >= threshold) ans++;
        }

        cout << ans << "\n";
    }
    return 0;
}
