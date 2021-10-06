"""
@Author: yanzx
@Date: 2021-10-06 15:30:28
@Desc: 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。


输入: a = 1, b = 1
输出: 2

解题思路：位运算


```java

class Solution {
    public int add(int a, int b) {
        int jinwei = b, bujinwei = a;
        while (b != 0){
            bujinwei = a ^ b;
            jinwei = (a & b) << 1;
            a = bujinwei;
            b = jinwei;
        }
        return a;
    }
}

```


"""


"""
 Python 没有 int , long 等不同长度变量，即在编程时无变量位数的概念。
获取负数的补码： 需要将数字与十六进制数 0xffffffff 相与。可理解为舍去此数字 32 位以上的数字（将 32 位以上都变为 00 ），从无限长度变为一个 32 位整数。
返回前数字还原： 若补码 aa 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。 a ^ x 运算将 1 至 32 位按位取反； ~ 运算是将整个数字取反；因此， ~(a ^ x) 是将 32 位以上的位取反，1 至 32 位不变。
"""


class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    s = Solution()
    res = s.add(-1, 2)
    print(res)
