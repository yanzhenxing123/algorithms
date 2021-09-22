"""
@Author: yanzx
@Date: 2021-09-22 08:18:37
@Desc:
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]

"""


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
            return None
        if num > self.arr[-1]:
            self.arr.append(num)
            return None
        for i in range(len(self.arr)):
            if num <= self.arr[i]:
                self.arr.insert(i, num)
                return None

    def findMedian(self) -> float:
        length = len(self.arr)
        if not length:
            return None
        if length % 2 == 1:
            return self.arr[length // 2]
        else:
            return (self.arr[length // 2] + self.arr[length // 2 - 1]) / 2


if __name__ == '__main__':
    finder = MedianFinder()
    finder.addNum(0)
    finder.addNum(0)
    res = finder.findMedian()
    print(res)
    finder.addNum(3)
    print(finder.findMedian())
