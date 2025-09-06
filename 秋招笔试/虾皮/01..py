"""

​赛马​​

​​详细描述​​

田忌与齐王赛马，两人各出n匹马，赛一场比赛得200两银子，
输了赔200两银子，平局不赔不赚(每匹马只能出场一次)。已知两人每匹马的速度，问田忌至多能够赢多少两银子。



您图片中的文字内容已为您识别并整理如下：

输入输出示例

示例1

输入
[20,30,40,50,60],[20,10,30,40,50]

输出
1000

说明
第一场：田忌20战胜齐王10，得200两
第二场：田忌30战胜齐王20，得200两
第三场：田忌40战胜齐王30，得200两
第四场：田忌50战胜齐王40，得200两
第五场：田忌60战胜齐王50，得200两
共赢5场，总计得1000两



"""


class Solution:
    def horseRace(self, tj, qw):
        tj.sort()
        qw.sort()
        n = len(tj)
        left_tj, right_tj = 0, n - 1
        left_qw, right_qw = 0, n - 1
        profit = 0
        while left_tj <= right_tj:
            if tj[right_tj] > qw[right_qw]:
                profit += 200
                right_tj -= 1
                right_qw -= 1
            elif tj[right_tj] < qw[right_qw]:
                profit -= 200
                left_tj += 1
                right_qw -= 1
            else:
                if tj[left_tj] < qw[left_qw]:
                    profit -= 200
                    left_tj += 1
                    right_qw -= 1
                else:
                    if tj[left_tj] == qw[left_qw]:
                        left_tj += 1
                        left_qw += 1
                    else:
                        profit += 200
                        left_tj += 1
                        left_qw += 1
        return profit


# 示例测试


if __name__ == "__main__":
    s = Solution()
    tian = [20, 30, 40, 50, 60]
    qi = [20, 10, 30, 40, 50]
    print(s.horseRace(tian, qi))
