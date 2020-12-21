import copy

from entity.Location import Location
from map_enum import Map
from push_enum import Push


class PushController:

    def __init__(self, map, monster_location):
        self.map = map
        self.monster_location = monster_location

    def push(self):
        tree_location = self._find_tree_location()
        map = self._push_tree(tree_location, self.monster_location.push_location)
        return map

    def _push_tree(self, tree_location, push_enum):
        # 获取移动几步
        move_step = self._get_tree_1_move_step(tree_location, push_enum)
        # 获取树的新位置
        new_tree_location = self._get_new_tree_location(tree_location, push_enum, move_step)
        # 获取移动后的地图
        map = self._get_moved_map(tree_location, new_tree_location)
        return map

    def _get_new_tree_location(self, tree_location, push_enum, move_step):
        new_tree_location = Location(tree_location.x, tree_location.y)
        if move_step == 0:
            return new_tree_location
        if push_enum == Push.up:
            new_tree_location.y = new_tree_location.y - move_step
        if push_enum == Push.down:
            new_tree_location.y = new_tree_location.y + move_step
        if push_enum == Push.left:
            new_tree_location.x = new_tree_location.x - move_step
        if push_enum == Push.right:
            new_tree_location.x = new_tree_location.x + move_step
        if tree_location.location_value == Map.tree1 or tree_location.location_value == Map.tree_stand:
            if push_enum == Push.up or push_enum == Push.down:
                if self.map[new_tree_location.y][new_tree_location.x] == Map.sea:
                    new_tree_location.location_value = Map.tree_vertical_1_sea
                else:
                    new_tree_location.location_value = Map.tree_vertical_1
            else:
                if self.map[new_tree_location.y][new_tree_location.x] == Map.sea:
                    new_tree_location.location_value = Map.tree_horizontal_1_sea
                else:
                    new_tree_location.location_value = Map.tree_horizontal_1
        return new_tree_location

    def _get_moved_map(self, old_tree_location, new_tree_location):
        new_map = copy.deepcopy(self.map)
        if old_tree_location.x == new_tree_location.x and old_tree_location.y == new_tree_location.y:
            return None
        if old_tree_location.location_value == Map.tree1:
            new_map[old_tree_location.y][old_tree_location.x] = Map.stump
        else:
            new_map[old_tree_location.y][old_tree_location.x] = Map.land
        new_map[new_tree_location.y][new_tree_location.x] = new_tree_location.location_value
        return new_map

    def _get_tree_1_move_step(self, tree_location, push_enum):
        move_step = 0
        # 如果树是立着的
        if tree_location.location_value == Map.tree_stand or tree_location.location_value == Map.tree1:
            move_step = 1
        # 如果树是横着的
        if tree_location.location_value == Map.tree_horizontal_1:
            # 如果树是左右推
            if push_enum == Push.right and push_enum == Push.left:
                move_step = 1
            else:
                move_step = self._find_tree1_left_right_push_step(tree_location, push_enum)
        # 如果树是竖着的
        if tree_location.location_value == Map.tree_vertical_1:
            # 如果树是上下推
            if push_enum == Push.up and push_enum == Push.down:
                move_step = 1
            else:
                move_step = self._find_tree1_up_down_push_step(tree_location, push_enum)
        return move_step

    def _find_tree1_up_down_push_step(self, tree_location, push_enum):
        temp_map = copy.deepcopy(self.map)
        temp_map = [[r[col] for r in temp_map] for col in range(len(temp_map[0]))]
        line = temp_map[tree_location.y]
        x = tree_location.x
        if push_enum == Push.down:
            line.reverse()
            x = len(line) - tree_location.x
        step = 0
        for i in range(x, len(line)):
            if line[i] == Map.land:
                step += 1
            elif line[i] == Map.sea:
                step += 1
                break
            else:
                break
        return step

    def _find_tree1_left_right_push_step(self, tree_location, push_enum):
        line = self.map[tree_location.y]
        x = tree_location.x
        if push_enum == Push.right:
            line.reverse()
            x = len(line) - tree_location.x
        step = 0
        for i in range(x, len(line)):
            if line[i] == Map.land:
                step += 1
            elif line[i] == Map.sea:
                step += 1
                break
            else:
                break
        return step

    def _find_tree_location(self):
        x = self.monster_location.x
        y = self.monster_location.y
        if self.monster_location.push_location == Push.up:
            y -= 1
        if self.monster_location.push_location == Push.down:
            y += 1
        if self.monster_location.push_location == Push.left:
            x -= 1
        if self.monster_location.push_location == Push.right:
            x += 1
        tree_location = Location(x, y)
        tree_location.location_value = self.map[tree_location.y][tree_location.x]
        return tree_location
