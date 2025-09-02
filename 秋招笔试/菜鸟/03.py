"""
@Author: yanzx
@Time: 2025/9/2 10:25 
@Description:

众所周知，在 Java 里可以利用重载的特性，用不同的参数调用同名方法。
小红依次尝试创建了 n 个方法，但其中的一些方法因为违背重载特性导致创建不成功。
你可以帮小红确认每个方法是否创建成功吗？

输入描述:
第一行输入一个正整数 n，代表小红创建的方法数量。
接下来的 n 行，每行输入一个字符串，包含方法的名称和参数。请注意，方法的主体（大括号内部的内容）已经省略。
1 ≤ n ≤ 5000
每个字符串长度不超过 80。保证每个方法都是合法的，一定包含返回类型、方法名、参数（或者无参）以及参数类型。



输出描述

对于每个方法，如果创建成功则输出"Yes"，否则输出"No"。

示例1

输入：

5
int f(int x)
void f()
int f()
int solve(Node node,int x)
int f(int y)

输出：
Yes
Yes
No
Yes
No

说明：
数据会有自定义类型。



"""

import re
def parse_method(method_str):
    """解析方法签名，返回(方法名, 参数类型列表)"""
    pattern = r'^(\w+)\s+(\w+)\s*\((.*)\)$'
    match = re.match(pattern, method_str.strip())
    if not match:
        return None, None
    return_type, method_name, params_str = match.groups()
    if params_str.strip() == "":
        param_types = []
    else:
        params = [p.strip() for p in params_str.split(',')]
        param_types = []
        for param in params:
            if '[' in param:
                type_part = param[:param.find('[') + 2]
            else:
                type_part = param.split()[-2] if len(param.split()) > 1 else param.split()[0]
            param_types.append(type_part)
    return method_name, param_types

def can_overload(method_name, param_types, existing_methods):
    """判断方法是否可以重载"""
    if method_name not in existing_methods:
        return True
    param_types_tuple = tuple(param_types)
    if param_types_tuple in existing_methods[method_name]:
        return False
    return True

def solve(n, method_strings):
    """解决Java方法重载问题"""
    existing_methods = {}
    results = []

    for method_str in method_strings:
        method_name, param_types = parse_method(method_str)

        if method_name is None:
            results.append("No")
            continue

        if can_overload(method_name, param_types, existing_methods):
            if method_name not in existing_methods:
                existing_methods[method_name] = set()
            existing_methods[method_name].add(tuple(param_types))
            results.append("Yes")
        else:
            results.append("No")

    return results

# 读取输入
n = int(input())
method_strings = []

for _ in range(n):
    method_str = input().strip()
    method_strings.append(method_str)

# 解决问题并输出结果
results = solve(n, method_strings)
for result in results:
    print(result)

