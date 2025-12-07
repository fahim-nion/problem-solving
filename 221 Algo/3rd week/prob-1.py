from collections import deque

R, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
visited = [[False]*H for _ in range(R)]

# Directions: up, down, left, right
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

max_diamonds = 0

for i in range(R):
    for j in range(H):
        if not visited[i][j] and grid[i][j] != '#':
            q = deque()
            q.append((i,j))
            visited[i][j] = True
            diamonds = 0
            if grid[i][j] == 'D':
                diamonds += 1
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < R and 0 <= ny < H:
                        if not visited[nx][ny] and grid[nx][ny] != '#':
                            visited[nx][ny] = True
                            if grid[nx][ny] == 'D':
                                diamonds += 1
                            q.append((nx, ny))
            max_diamonds = max(max_diamonds, diamonds)

print(max_diamonds)
