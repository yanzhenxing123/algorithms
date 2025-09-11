"""
@Time: 2025/9/11 22:23
@Author: yanzx
@Description:

根据您提供的两张图片内容，以下是提取的文字信息整理：

题目名称：选配专家
时间限制：1000ms
内存限制：256M
编程语言环境：Python3
系统提示：编程题部分已开启禁止切出页面限制，请勿使用本地IDE调试。

题目背景描述：

为了提升用户在选购云服务器时的体验，浪潮计划开发一款云服务器选配推荐工具。该工具将依据用户总的需求CPU核数和内存大小，提供匹配的云服务器规格配置组合建议。已知不同规格云服务器配置如下：

规格 配置（CPU核数, 内存大小） 价格（元/每月）

S1_small_1 1个CPU, 1GiB内存 33.8

S1_medium_2 1个CPU, 2GiB内存 74.1

S1_large_1 2个CPU, 2GiB内存 143

S1_large_2 2个CPU, 4GiB内存 172

S1_xlarge_1 4个CPU, 4GiB内存 303
S1_xlarge_2 4个CPU, 8GiB内存 338.3
输入输出要求：

输入描述：
输入包含多组测试数据，每一行包含逗号分隔的CPU核数和内存大小（例如：32,64 表示32核、64GiB内存）。

输出描述：
在每一行中输出满足需求的配置组合中每月花费总额最少的组合对应的金额数（单位：元），若不存在满足条件的配置组合则返回0。

示例：
示例输入：4,8
示例输出：296.4



"""


def main():
    # 定义服务器规格列表：每个规格包含(cpu, memory, price)
    servers = [
        (1, 1, 33.8),  # S1_small_1
        (1, 2, 74.1),  # S1_medium_2
        (2, 2, 143),  # S1_large_1
        (2, 4, 172),  # S1_large_2
        (4, 4, 303),  # S1_xlarge_1
        (4, 8, 338.3)  # S1_xlarge_2
    ]

    while True:
        try:
            # 读取输入
            data = input().strip()
            if not data:
                continue

            # 解析CPU和内存需求
            cpu_need, memory_need = map(int, data.split(','))

            # 初始化动态规划数组
            # dp[i][j] = 满足i个CPU和jGiB内存的最小花费
            # 使用浮点数初始化，初始值为一个很大的数
            INF = float('inf')
            dp = [[INF] * (memory_need + 1) for _ in range(cpu_need + 1)]
            dp[0][0] = 0  # 0个CPU和0GiB内存的花费为0

            # 动态规划处理
            for i in range(cpu_need + 1):
                for j in range(memory_need + 1):
                    if dp[i][j] == INF:
                        continue

                    # 尝试选择每种服务器规格
                    for cpu, mem, price in servers:
                        new_i = i + cpu
                        new_j = j + mem
                        # 只能精确满足目标，不能超配
                        if new_i <= cpu_need and new_j <= memory_need:
                            if dp[new_i][new_j] > dp[i][j] + price:
                                dp[new_i][new_j] = dp[i][j] + price

            # 获取结果
            result = dp[cpu_need][memory_need]

            # 输出结果，如果无解则输出0
            if result == INF:
                print(0)
            else:
                # 保留一位小数（根据示例输出格式）
                print("{:.1f}".format(result))

        except EOFError:
            break
        except:
            print(0)


if __name__ == "__main__":
    main()