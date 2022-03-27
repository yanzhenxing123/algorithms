class Solution:
    def getNums(self, n: int, max: int) -> int:
        ans = 1
        left = n * 10 + 0
        right = n * 10 + 9
        while max >= left:
            if max <= right:
                ans += max - left + 1
            else:
                ans += right - left + 1
            left = left * 10 + 0
            right = right * 10 + 9
        return ans

    def findKthNumber(self, n: int, k: int) -> int:
        l = 1
        r = 9
        while k:
            for i in range(l, r + 1):
                num = self.getNums(i, n)
                if k > num:
                    k -= num
                else:
                    k -= 1
                    if k == 0:
                        return i
                    l = i * 10 + 0
                    r = i * 10 + 9
                    break
        return 0

s = Solution()
n = int(input())
for i in range(1, 51):
    res = s.findKthNumber(n, i)
    tmp = str(res) + ".mp4"
    print(tmp)