#!/bin/bash

echo "=== 编译C++代码 ==="

# 编译基础版本
echo "编译基础版本..."
g++ -O2 -std=c++17 -o triplet_count triplet_count.cpp

# 编译高级版本
echo "编译高级版本..."
g++ -O2 -std=c++17 -o triplet_count_advanced triplet_count_advanced.cpp

echo "编译完成！"
echo ""

echo "=== 测试基础版本 ==="
echo "测试用例1: [1, 5, 4, 2, 3]"
echo "5
1 5 4 2 3" | ./triplet_count

echo ""
echo "测试用例2: [4, 1, 2, 3]"
echo "4
4 1 2 3" | ./triplet_count

echo ""
echo "=== 测试高级版本 ==="
echo "测试用例1: [1, 5, 4, 2, 3]"
echo "5
1 5 4 2 3" | ./triplet_count_advanced

echo ""
echo "测试用例2: [4, 1, 2, 3]"
echo "4
4 1 2 3" | ./triplet_count_advanced

echo ""
echo "=== 性能测试 ==="
echo "生成大数组进行性能测试..."

# 生成大数组测试数据
python3 -c "
n = 1000
arr = list(range(n, 0, -1)) + list(range(1, n+1))
print(n)
print(' '.join(map(str, arr)))
" > large_input.txt

echo "测试大数组 (2000个元素)..."
time ./triplet_count < large_input.txt
time ./triplet_count_advanced < large_input.txt

echo ""
echo "测试完成！"
