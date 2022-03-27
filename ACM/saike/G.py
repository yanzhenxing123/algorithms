def get_n(n, max) -> int:
    ans = 1
    l = n * 10 + 0
    r = n * 10 + 9
    while max >= l:
        if max <= r:
            ans += max - l + 1
        else:
            ans += r - l + 1
        l = l * 10 + 0
        r = r * 10 + 9
    return ans

def find_k_num(n, k) -> int:
    l = 1
    r = 9
    while k:
        for i in range(l, r + 1):
            num = get_n(i, n)
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

n = int(input())
for i in range(1, 51):
    res = find_k_num(n, i)
    tmp = str(res) + ".mp4"
    print(tmp)