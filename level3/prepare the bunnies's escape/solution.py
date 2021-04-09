# def solution(map):
# 
#     def dfs(i,j,prev_cost,removed):
# 
#         if(i<0 or i>=len(map) or j<0 or j>=len(map[0])):
#             return
#         if(map[i][j]==1 and removed>=1):
#             return
#         if(removed==0 and prev_cost>=dp[0][i][j]):
#             return
#         if(removed==1 and (prev_cost>=dp[0][i][j] or prev_cost>=dp[1][i][j])):
#             return
#         if(map[i][j]==0):
#             dp[removed][i][j] = prev_cost+1
#             dfs(i+1,j,prev_cost+1,removed)
#             dfs(i-1,j,prev_cost+1,removed)
#             dfs(i,j+1,prev_cost+1,removed)
#             dfs(i,j-1,prev_cost+1,removed)
#         else:
#             #map[i][j]==1 and removed ==0
#             dp[removed][i][j] = prev_cost+1
#             dfs(i+1,j,prev_cost+1,removed+1)
#             dfs(i-1,j,prev_cost+1,removed+1)
#             dfs(i,j+1,prev_cost+1,removed+1)
#             dfs(i,j-1,prev_cost+1,removed+1)
# 
#     dp  =[[[10000]*len(map[0]) for i in range(len(map))] for j in range(2)]
#     dfs(0,0,0,0)
# 
#     return min(dp[0][len(map)-1][len(map[0])-1],dp[1][len(map)-1][len(map[0])-1])


def calc_distance(sx, sy, map):
    w = len(map[0])
    h = len(map)
    board = [[None for i in range(w)] for i in range(h)]
    board[sx][sy] = 1

    arr = [(sx, sy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx, ny = x + i[0], y + i[1]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] is None:
                    board[nx][ny] = board[x][y] + 1
                    if map[nx][ny] == 1:
                        continue
                    arr.append((nx, ny))

    return board


def solution(map):
    #we will assume map[i][j] has the wall that we need to remove
    #if map[i][j]==0, that is normal recursion
    w = len(map[0])
    h = len(map)
    to_loc = calc_distance(0, 0, map)
    from_loc = calc_distance(h - 1, w - 1, map)
    board = []

    ans = 2 ** 32 - 1
    for i in range(h):
        for j in range(w):
            if to_loc[i][j] and from_loc[i][j]:
                ans = min(to_loc[i][j] + from_loc[i][j] - 1, ans)
    return ans



print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))