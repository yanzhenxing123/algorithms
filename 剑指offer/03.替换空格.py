"""
@Author: yanzx
@Date: 2021/4/5 10:56
@Description: 
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for split in s:
            if split == " ":
                res.append("%20")
            else:
                res.append(split)
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    res = s.replaceSpace("we are happy")
    print(res)
