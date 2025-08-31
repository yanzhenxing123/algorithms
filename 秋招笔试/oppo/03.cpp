#include <bits/stdc++.h>
using namespace std;

// 检查数组是否单调不降
bool isMonotonic(const vector<int>& arr) {
    for (int i = 1; i < (int)arr.size(); i++) {
        if (arr[i] < arr[i - 1]) return false;
    }
    return true;
}

int minDeleteOperations(int n, const vector<int>& arr) {
    // 找到所有不同的值
    vector<int> uniqueVals = arr;
    sort(uniqueVals.begin(), uniqueVals.end());
    uniqueVals.erase(unique(uniqueVals.begin(), uniqueVals.end()), uniqueVals.end());

    int m = uniqueVals.size();
    int minDel = m; // 最坏情况：删除所有不同值

    // 枚举删除多少种数
    for (int delCnt = 0; delCnt <= m; delCnt++) {
        // 枚举删除集合的所有组合
        vector<int> mask(m, 0);
        fill(mask.begin(), mask.begin() + delCnt, 1);
        do {
            unordered_set<int> toDelete;
            for (int i = 0; i < m; i++) {
                if (mask[i]) toDelete.insert(uniqueVals[i]);
            }
            // 构造剩余数组
            vector<int> remaining;
            for (int v : arr) {
                if (!toDelete.count(v)) remaining.push_back(v);
            }
            // 检查是否单调不降
            if (isMonotonic(remaining)) {
                return delCnt; // 找到最小解直接返回
            }
        } while (prev_permutation(mask.begin(), mask.end()));
    }

    return minDel;
}

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
        cout << minDeleteOperations(n, arr) << "\n";
    }
    return 0;
}
