from entity.Location import Location
from map_controller.push_controller import PushController
from map_controller.road_controller import RoadController
from map_enum import Map
from program_helper.print_helper import Log
from push_enum import Push


class PlayController:

    def __init__(self, map, end_points, current_monster_point):
        self.map = map
        self.end_points = end_points
        self.current_monster_point = current_monster_point

    def find_monster_near_by_tree_locations(self):
        # 先找到所有的树
        trees = self._find_all_tree_locations()
        # 再找到树旁边所有可以站立小怪兽的地方
        monsters = self._find_all_monster_locations(trees)
        # 过滤出小怪兽可以达到的所有位置
        monsters_arrived = self._find_monster_arrive_locations(monsters)
        # 返回一个数组
        return monsters_arrived

    def monster_push_tree(self, monster_location):
        new_monster_location = Location(
            monster_location.x,
            monster_location.y,
            monster_location.location_value,
        )
        able_to_push, new_map = self._push_tree_1(monster_location)
        return new_map, new_monster_location, able_to_push

    def _push_tree_1(self, monster_location):
        push_controller = PushController(self.map, monster_location)
        map = push_controller.push()
        if not map:
            return False, map
        return True, map

    # def _push_tree_2(self, push_value):
    #     return False, self.map

    # @staticmethod
    # def _is_tree_1(location_value):
    #     if location_value == Map.tree1:
    #         return True
    #     if location_value == Map.tree_stand:
    #         return True
    #     if location_value == Map.tree_horizontal_1:
    #         return True
    #     if location_value == Map.tree_vertical_1:
    #         return True
    #     return False
    #
    # @staticmethod
    # def _is_tree_2(location_value):
    #     if location_value == Map.tree2:
    #         return True
    #     if location_value == Map.tree_horizontal_2:
    #         return True
    #     if location_value == Map.tree_vertical_2:
    #         return True
    #     return False

    def success_result(self):
        print('succeed')
        Log.map(self.map)

    def is_success(self):
        successes = []
        for end_point in self.end_points:
            point = self.map[end_point.y][end_point.x]
            if end_point.location_value == Map.end_horizontal:
                if point == Map.end_horizontal_1:
                    successes.append(True)
            if end_point.location_value == Map.end_horizontal:
                if point == Map.end_horizontal_1:
                    successes.append(True)
            if end_point.location_value == Map.end_double:
                if point == Map.end_double_2:
                    successes.append(True)
        if len(successes) == len(self.end_points):
            for success in successes:
                if not success:
                    return False
        else:
            return False
        return True

    def _find_monster_arrive_locations(self, monster_locations):
        monsters_arrived = []
        for monster_goto_location in monster_locations:
            road_controller = RoadController(self.map, self.current_monster_point, monster_goto_location)
            if road_controller.is_arrived():
                monsters_arrived.append(monster_goto_location)
        return monsters_arrived

    def _find_all_monster_locations(self, trees):
        all_monster_locations = []
        for tree in trees:
            x = tree.x
            y = tree.y
            locations = [
                Location(x-1, y, self.map[y][x-1], Push.right),  # 左边的
                Location(x+1, y, self.map[y][x+1], Push.left),  # 右边的
                Location(x, y-1, self.map[y-1][x], Push.down),  # 上边的
                Location(x, y+1, self.map[y+1][x], Push.up),  # 下边的
            ]
            for location in locations:
                map_type = self.map[location.y][location.x]
                if map_type == Map.land:  # 如果是在陆地上
                    all_monster_locations.append(location)
                if map_type == Map.stump:  # 如果是在树桩上
                    all_monster_locations.append(location)
                if map_type == Map.tree_horizontal_1_sea:  # 单节长度 横着的 海中的 木棍
                    all_monster_locations.append(location)
                if map_type == Map.tree_vertical_1_sea:  # 单节长度 竖着的 海中的 木棍
                    all_monster_locations.append(location)
                if map_type == Map.tree_horizontal_2_sea:  # 双节长度 横着的 海中的 木棍
                    all_monster_locations.append(location)
                if map_type == Map.tree_vertical_2_sea:  # 双节长度 竖着的 海中的 木棍
                    all_monster_locations.append(location)
        return all_monster_locations

    def _find_all_tree_locations(self):
        trees_location = []
        y = 0
        for line in self.map:
            x = 0
            for value in line:
                if value == Map.tree1 or \
                        value == Map.tree2 or \
                        value == Map.tree_horizontal_1 or \
                        value == Map.tree_vertical_1:
                    tree = Location(x, y)
                    tree.location_value = value
                    trees_location.append(tree)
                x += 1
            y += 1
        return trees_location
