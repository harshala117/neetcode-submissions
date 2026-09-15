class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        seen = set()
        count = 0

        directions = [ 
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        def bfs(r, c):
            queue = deque([(r, c)])
            seen.add((r, c))

            while queue:
                row, col = queue.popleft() # remove and check for neighbour 

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if(
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        queue.append((nr, nc))
        for r in range(rows): # check every single cell
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in seen: # see if this cell is land and have I ever visited it
                    bfs(r, c)
                    count += 1 # discover new island as land is unvisited 
        return count
     
        
        