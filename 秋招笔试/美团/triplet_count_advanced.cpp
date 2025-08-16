#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;

typedef long long ll;

// 使用有序集合（红黑树）优化
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

// 高级优化版本：使用有序集合
ll count_triplets_advanced(vector<int>& arr) {
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
            // 使用二分查找
            count += lower_bound(right_greater.begin(), right_greater.end(), ai) - right_greater.begin();
        }
    }
    return count;
}

// 终极C++优化版本
ll count_triplets_ultimate_cpp(vector<int>& arr) {
    int n = arr.size();
    ll count = 0;
    
    for (int j = 1; j < n - 1; j++) {
        int aj = arr[j];
        
        // 预分配空间
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

// 混合策略版本
ll count_triplets_hybrid_cpp(vector<int>& arr) {
    int n = arr.size();
    
    // 对于小数组，使用简单版本
    if (n <= 100) {
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
    
    // 对于大数组，使用优化版本
    return count_triplets_ultimate_cpp(arr);
}

int main() {
    // 优化输入输出
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    // 使用混合策略版本
    ll result = count_triplets_hybrid_cpp(arr);
    cout << result << endl;
    
    return 0;
}
