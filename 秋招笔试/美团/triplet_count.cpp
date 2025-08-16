#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

typedef long long ll;

// 原始版本：三重循环
ll count_triplets_original(vector<int>& arr) {
    int n = arr.size();
    ll count = 0;
    
    for (int j = 1; j < n - 1; j++) {
        int aj = arr[j];
        for (int i = 0; i < j; i++) {
            int ai = arr[i];
            if (ai > aj) {
                for (int k = j + 1; k < n; k++) {
                    int ak = arr[k];
                    if (ak > aj && ak < ai) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}

// 优化版本：使用二分查找
ll count_triplets_optimized(vector<int>& arr) {
    int n = arr.size();
    ll count = 0;
    
    for (int j = 1; j < n - 1; j++) {
        int aj = arr[j];
        
        // 收集左边大于aj的元素
        vector<int> left_greater;
        for (int i = 0; i < j; i++) {
            if (arr[i] > aj) {
                left_greater.push_back(arr[i]);
            }
        }
        
        // 收集右边大于aj的元素
        vector<int> right_greater;
        for (int k = j + 1; k < n; k++) {
            if (arr[k] > aj) {
                right_greater.push_back(arr[k]);
            }
        }
        
        // 排序右边元素
        sort(right_greater.begin(), right_greater.end());
        
        // 对于每个左边的元素ai
        for (int ai : left_greater) {
            // 使用二分查找找到右边小于ai的元素数量
            int pos = lower_bound(right_greater.begin(), right_greater.end(), ai) - right_greater.begin();
            count += pos;
        }
    }
    return count;
}

// 终极优化版本：使用STL优化
ll count_triplets_ultimate(vector<int>& arr) {
    int n = arr.size();
    ll count = 0;
    
    for (int j = 1; j < n - 1; j++) {
        int aj = arr[j];
        
        // 使用vector预分配空间，避免频繁重新分配
        vector<int> left_greater, right_greater;
        left_greater.reserve(j);
        right_greater.reserve(n - j - 1);
        
        // 收集左边大于aj的元素
        for (int i = 0; i < j; i++) {
            if (arr[i] > aj) {
                left_greater.push_back(arr[i]);
            }
        }
        
        // 收集右边大于aj的元素
        for (int k = j + 1; k < n; k++) {
            if (arr[k] > aj) {
                right_greater.push_back(arr[k]);
            }
        }
        
        // 排序右边元素
        sort(right_greater.begin(), right_greater.end());
        
        // 对于每个左边的元素ai
        for (int ai : left_greater) {
            // 使用STL的二分查找
            count += lower_bound(right_greater.begin(), right_greater.end(), ai) - right_greater.begin();
        }
    }
    return count;
}

// 混合优化版本：根据数组大小选择策略
ll count_triplets_hybrid(vector<int>& arr) {
    int n = arr.size();
    
    // 对于小数组，使用原始版本
    if (n <= 100) {
        return count_triplets_original(arr);
    }
    
    // 对于大数组，使用终极优化版本
    return count_triplets_ultimate(arr);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    // 使用终极优化版本
    ll result = count_triplets_ultimate(arr);
    cout << result << endl;
    
    return 0;
}
