#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 合并重叠的区间
vector<pair<int, int>> mergeIntervals(vector<pair<int, int>>& intervals) {
    if (intervals.empty()) {
        return {};
    }
    
    // 按开始时间排序
    sort(intervals.begin(), intervals.end());
    
    vector<pair<int, int>> merged;
    merged.push_back(intervals[0]);
    
    for (size_t i = 1; i < intervals.size(); i++) {
        // 如果当前区间与最后一个合并区间重叠，则合并
        if (intervals[i].first <= merged.back().second + 1) { // +1 因为时间点是连续的整数
            merged.back().second = max(merged.back().second, intervals[i].second);
        } else {
            merged.push_back(intervals[i]);
        }
    }
    
    return merged;
}

// 计算可用的维修时间
long long calculateAvailableTime(int H, vector<pair<int, int>>& warningPeriods) {
    if (warningPeriods.empty()) {
        return H;
    }
    
    // 合并重叠的预警时段
    vector<pair<int, int>> mergedWarnings = mergeIntervals(warningPeriods);
    
    // 计算被预警时段覆盖的总时间
    long long coveredTime = 0;
    for (const auto& period : mergedWarnings) {
        coveredTime += period.second - period.first + 1;
    }
    
    // 可用时间 = 总时间 - 被覆盖时间
    long long availableTime = H - coveredTime;
    
    return max(0LL, availableTime);
}

// 解决道路维修时间计算问题
void solveRoadMaintenance() {
    int T; // 测试用例数量
    cin >> T;
    
    for (int t = 0; t < T; t++) {
        int H; // 总工作时间
        int N; // 预警时段数量
        cin >> H >> N;
        
        vector<pair<int, int>> warningPeriods;
        for (int i = 0; i < N; i++) {
            int xi, yi;
            cin >> xi >> yi;
            warningPeriods.push_back({xi, yi});
        }
        
        // 计算并输出结果
        long long result = calculateAvailableTime(H, warningPeriods);
        cout << result << endl;
    }
}

// 测试函数
void testExample() {
    cout << "测试示例:" << endl;
    cout << "输入:" << endl;
    cout << "1" << endl;
    cout << "10" << endl;
    cout << "2" << endl;
    cout << "5 10" << endl;
    cout << "5 5" << endl;
    cout << endl;
    cout << "预期输出: 4" << endl;
    cout << endl;
    
    // 模拟输入
    int H = 10;
    vector<pair<int, int>> warningPeriods = {{5, 10}, {5, 5}};
    
    long long result = calculateAvailableTime(H, warningPeriods);
    cout << "实际输出: " << result << endl;
    cout << "测试" << (result == 4 ? "通过" : "失败") << endl;
}

int main() {
    // 运行测试
    testExample();
    cout << "\n" << string(50, '=') << endl;
    cout << "运行主程序:" << endl;
    cout << "请输入测试用例数据:" << endl;
    
    // 运行主程序
    solveRoadMaintenance();
    
    return 0;
}
