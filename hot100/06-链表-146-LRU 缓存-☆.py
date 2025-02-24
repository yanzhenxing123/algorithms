"""
@Time: 2024/4/13 15:30
@Author: yanzx
@Desc:
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

设计思路：
1. 常规：双端链表 + hash表
2. 使用字典（python3.6之后变得有序，使用iter进行删除元素）, 访问过和新加入的都放到最后
3. 继承OrderedDict(有序字典)，使用popitem和move_to_end
"""
import collections


class LRUCache2:
    """
    使用字典（python3.6之后变得有序，使用iter进行删除元素）, 访问过和新加入的都放到最后
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}

    def get(self, key: int) -> int:
        if key in self.data:
            value = self.data.pop(key)
            self.data[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:  # 1. 如果key存在则更新
            self.data.pop(key)
            self.data[key] = value
        else:  # 不存在：a.未满 b.已满
            if self.capacity == len(self.data):  # 超过capacity则删除第一个元素
                k = next(iter(self.data))  # 返回key
                self.data.pop(k)
            self.data[key] = value


# 同时维护双端链表和哈希表
class ListNode:
    def __init__(self, key, value):
        self.key = key  # 键
        self.value = value  # 值
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.pre = self.tail
        self.tail.next = self.head
        self.hash_map = {}

    def move_to_end(self, node: ListNode):
        # 将给定的node放到尾部
        if self.tail.pre is None:  # 如果为第一个数据
            self.head.next = node
            node.pre = self.head
        else:
            self.tail.pre.next = node
            node.pre = self.tail.pre

        node.next = self.tail
        self.tail.pre = node

    def get(self, key: int) -> int:
        # 如果字典中存在该键 就将字典中的值返回 并将这个节点放到双端链表的最后面
        node = self.hash_map.get(key)
        if not node:
            return -1
        # 如果为最后一个就不用动了
        if node.next == self.tail:
            return node.value

        # 先删除 再插到最后
        node.pre.next = node.next
        node.next.pre = node.pre
        self.move_to_end(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 如果存在该键，则更新
        if self.get(key) != -1:
            # 更新字段
            self.hash_map[key].value = value
            return
        # 如果不存在 那么添加到链表的尾部
        # 满了删除表头 同时删除字典中的键
        if len(self.hash_map) == self.capacity:
            delete_node = self.head.next
            self.head.next = self.head.next.next
            self.head.next.pre = self.head
            self.hash_map.pop(delete_node.key)

        # 将节点放到插到尾部
        node = ListNode(key, value)
        self.hash_map[key] = node
        self.move_to_end(node)

    # 打印过程
    def show(self):
        p = self.head.next
        print("head->", end="")
        while p != self.tail:
            print(p.key, end="->")
            p = p.next
        print("tail")


class LRUCache3(collections.OrderedDict):
    """
    继承OrderedDict，也是将访问过的放到最后
    """

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)  # 放到最后
        return self.get(key)

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)  # 表示FIFO


if __name__ == '__main__':
    capacity = 5
    obj = LRUCache2(capacity)
    obj.put(1, 100)
    obj.put(2, 200)
    obj.put(3, 300)
    obj.put(4, 400)
    obj.put(5, 500)
    obj.put(6, 600)
