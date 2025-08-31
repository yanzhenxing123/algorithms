"""
@Time: 2025/8/31 16:39
@Author: yanzx
@Description:


示例1

输入：

3 3 2
aaa
aba


输出：
4


说明

由A和B构成的矩形C为：
aba
aba
aba
所以有四个子矩形全都为a且字符总数为2。



示例1

输入：

3 6 4
aaa
aaaaaa


输出：
19
"""



def count_substrings(s):
    """统计字符串中连续 'a' 段的长度"""
    res = []
    cnt = 0
    for ch in s:
        if ch == 'a':
            cnt += 1
        else:
            if cnt > 0:
                res.append(cnt)
                cnt = 0
    if cnt > 0:
        res.append(cnt)
    return res


def calc_f(segments, x):
    """计算 f(x): 在所有连续 'a' 段中，长度 >= x 的部分贡献"""
    total = 0
    for length in segments:
        if length >= x:
            total += length - x + 1
    return total


def solve():
    import sys
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    A = input().strip()
    B = input().strip()

    segA = count_substrings(A)
    segB = count_substrings(B)

    ans = 0
    # 遍历 k 的所有因子
    i = 1
    while i * i <= k:
        if k % i == 0:
            x, y = i, k // i
            ans += calc_f(segA, x) * calc_f(segB, y)
            if x != y:  # 避免平方数重复计算
                ans += calc_f(segA, y) * calc_f(segB, x)
        i += 1

    print(ans)


if __name__ == "__main__":
    solve()
