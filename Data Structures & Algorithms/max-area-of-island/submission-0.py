from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()

        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        max_area = 0

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            seen.add((sr, sc))

            area = 0

            while q:
                r, c = q.popleft()
                area += 1

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        q.append((nr, nc))

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = bfs(r, c)
                    max_area = max(max_area, area)

        return max_area