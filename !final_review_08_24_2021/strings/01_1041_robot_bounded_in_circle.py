class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0 deg: north, 90 deg: left, 180 deg: down, 270 deg: right, 360 deg: north
        # uldr
        directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        cur_direction = 0
        cur_y = 0
        cur_x = 0
        for instruction in instructions:
            if instruction == "L":
                cur_direction = self.switchDirection(cur_direction, 1)
            elif instruction == "R":
                cur_direction = self.switchDirection(cur_direction, -1)
            elif instruction == "G":
                new_direction = directions[cur_direction]
                cur_y += new_direction[0]
                cur_x += new_direction[1]
        return cur_y == 0 and cur_x == 0 or cur_direction != 0

    def switchDirection(self, cur, nxt):
        tmp = cur + nxt
        if tmp < 0:
            return 3
        return (cur + nxt) % 4