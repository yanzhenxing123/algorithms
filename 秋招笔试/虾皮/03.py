"""
@Author: yanzx
@Time: 2025/8/20 17:34 
@Description: 
"""



#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 计算最大区域
# @param arr int整型 二维数组 地图
# @return int整型
#
from curses import noraw


class Solution:
    def closure(self, arr) :
        # write code here
        grid = arr
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        all_ones = True
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    all_ones = False
                    break
            if not all_ones:
                break
        if all_ones:
            return rows * cols
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    new_grid = [row[:] for row in grid]
                    new_grid[i][j] = 1
                    
                    visited = [[False] * cols for _ in range(rows)]
                    current_max = 0
                    
                    for x in range(rows):
                        for y in range(cols):
                            if new_grid[x][y] == 1 and not visited[x][y]:
                                stack = [(x, y)]
                                visited[x][y] = True
                                area = 0
                                
                                while stack:
                                    cx, cy = stack.pop()
                                    area += 1
                                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                        nx, ny = cx + dx, cy + dy
                                        if 0 <= nx < rows and 0 <= ny < cols and new_grid[nx][ny] == 1 and not visited[nx][ny]:
                                            stack.append((nx, ny))
                                            visited[nx][ny] = True
                                            
                                current_max = max(current_max, area)
                        max_area = max(max_area, current_max)
        return max_area


if __name__ == '__main__':
    s = Solution()
    arr1 = [[1, 1], [1, 1]]
    res = s.closure(arr1)
    print(res)

    arr2 = [[1,0],[0,1]]
    res = s.closure(arr2)
    print(res)