import collections
import sys

INF = 2147483647

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    q = collections.deque()
    for i in range(len(dungeon_map)):
        for j in range(len(dungeon_map[i])):
            if dungeon_map[i][j] == 0:
                q.append((i, j))
    level = 1
    #ULDR
    y_dir = [1,0,-1,0]
    x_dir = [0,-1,0,1]
    while q:
        for i in range(len(q)):
            cur_y, cur_x = q.popleft()
            for j in range(len(y_dir)):
                new_y, new_x = cur_y + y_dir[j], cur_x + x_dir[j]
                if 0 <= new_y < len(dungeon_map) and 0 <= new_x < len(dungeon_map[0]):
                    if dungeon_map[new_y][new_x] == INF:
                        dungeon_map[new_y][new_x] = level
                        q.append((new_y, new_x))
        level += 1
    return dungeon_map