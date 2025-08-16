"""
@Time: 2025/8/16 10:16
@Author: yanzx
@Description:


问题分析
题目要求重新排列数组，使得权值 ∑
i=2
n
​
 (a
i
​
 +a
i−1
​
 )达到最大和最小。我们需要找到排列方式使得相邻元素之和的总和最大化或最小化。

关键观察
1.
​​权值展开​​：

i=2
∑
n
​
 (a
i
​
 +a
i−1
​
 )=(a
2
​
 +a
1
​
 )+(a
3
​
 +a
2
​
 )+⋯+(a
n
​
 +a
n−1
​
 )=2
i=1
∑
n
​
 a
i
​
 −a
1
​
 −a
n
​

因此，权值实际上等于 2×数组总和−首元素−尾元素。

2.
​​最大化权值​​：

∙
为了使权值最大，需要最小化 a
1
​
 +a
n
​
 。

∙
因此，将最小的两个元素放在首尾。

3.
​​最小化权值​​：

∙
为了使权值最小，需要最大化 a
1
​
 +a
n
​
 。

∙
因此，将最大的两个元素放在首尾。
"""

n = int(input())
a = list(map(int, input().split()))
total = sum(a)

# 排序数组
a_sorted = sorted(a)

# 最大权值：最小两个元素在首尾
max_weight = 2 * total - a_sorted[0] - a_sorted[1]

# 最小权值：最大两个元素在首尾
min_weight = 2 * total - a_sorted[-1] - a_sorted[-2]

print(max_weight, min_weight)