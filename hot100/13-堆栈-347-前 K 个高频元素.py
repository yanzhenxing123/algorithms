"""
@Time: 2024/8/20 14:36
@Author: yanzx
@Desc: 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。


"""

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        heapq存储二元组时，会按照第一个元素构建小根堆
        :param nums:
        :param k:
        :return:
        """
        counter = Counter(nums)
        min_heap = []
        for num, freq in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                if min_heap[0][0] < freq:
                    heapq.heapreplace(min_heap, (freq, num))

        res = [item[1] for item in min_heap]
        return res

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(items[i][0])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    s.topKFrequent(nums, k)
