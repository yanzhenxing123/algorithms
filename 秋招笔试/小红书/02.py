"""
@Time: 2025/8/17 19:57
@Author: yanzx
@Description: 
"""


# def count_commented_plogs(n, s):
#     queue = list(s)
#     res = 0
#     while True:
#         to_remove = set()
#         # Find all Plogs to be commented in this round
#         for i in range(len(queue)):
#             if i + 1 < len(queue):
#                 j = i + 1
#                 while j < len(queue) and queue[j] == queue[i]:
#                     j += 1
#                 if j < len(queue) and queue[j] != queue[i]:
#                     to_remove.add(j)
#         if not to_remove:
#             break
#         res += len(to_remove)
#         # Remove commented Plogs
#         new_queue = []
#         for i in range(len(queue)):
#             if i not in to_remove:
#                 new_queue.append(queue[i])
#         queue = new_queue
#     return res



def count_commented_plogs(n, s):
    s = list(s)
    removed = [False] * n
    from collections import deque
    q = deque()

    # 先找初始可以删的位置
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            q.append(i + 1)

    res = 0
    while q:
        idx = q.popleft()
        if removed[idx]:
            continue
        removed[idx] = True
        res += 1

        # 删除 idx 后，看看左右是否新形成一对
        left, right = idx - 1, idx + 1
        while left >= 0 and removed[left]:
            left -= 1
        while right < n and removed[right]:
            right += 1
        if left >= 0 and right < n and s[left] != s[right]:
            q.append(right)

    return res


# Test cases
print(count_commented_plogs(5, "11101"))  # Output: 2
print(count_commented_plogs(10, "1100010101"))  # Output: 8
