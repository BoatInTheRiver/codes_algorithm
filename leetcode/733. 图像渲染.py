#coding:utf-8

'''
输入:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
解析:
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。

'''
import collections
class Solution:
    # 深度优先遍历DFS
    def floodFill(self, image, sr, sc, newColor):
        originalColor = image[sr][sc]
        if originalColor != newColor:
            self.dfs(image, sr, sc, originalColor, newColor)
        return image

    def dfs(self, image, x, y, originalColor, newColor):
        if not 0 <= x < len(image) or not 0 <= y < len(image[0]):
            return
        if image[x][y] == originalColor:
            image[x][y] = newColor
            self.dfs(image, x + 1, y, originalColor, newColor)
            self.dfs(image, x - 1, y, originalColor, newColor)
            self.dfs(image, x, y - 1, originalColor, newColor)
            self.dfs(image, x, y + 1, originalColor, newColor)


    # 广度优先遍历BFS
    def floodFill1(self, image, sr, sc, newColor):
        originalColor = image[sr][sc]
        if originalColor == newColor:
            return image
        queue = collections.deque()
        queue.append((sr, sc))
        while queue:
            x, y = queue.popleft()
            if not 0 <= x < len(image) or not 0 <= y < len(image[0]) or image[x][y] != originalColor:
                continue
            image[x][y] = newColor
            queue.extend([(x-1,y), (x+1, y), (x, y-1), (x, y+1)])
        return image