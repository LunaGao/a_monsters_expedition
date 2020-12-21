from entity.Location import Location
from map_controller.play_controller import PlayController
from map_enum import Map
from program_helper.print_helper import Log


class GameController:
    map = []
    deep_count = 5
    start_location = Location(0, 0)
    end_locations = []

    def __init__(self, map):
        self.map = map

    def play_game(self, deep_count):
        self.deep_count = deep_count
        self._find_start_location()
        self._find_end_location()
        Log.location(self.start_location)
        Log.locations(self.end_locations)
        self._play(self.map, 0, self.start_location)

    def _play(self, map, play_count, monster_location):
        play_controller = PlayController(map, self.end_locations, monster_location)
        # 检查是否已经成功推到位置
        if play_controller.is_success():
            print(play_controller.success_result())
            return
        # 如果递归超过deep count，则不再进行计算
        if play_count > self.deep_count:
            return
        # 找到树旁边可以站小怪兽的地方
        monster_near_by_trees_locations = play_controller.find_monster_near_by_tree_locations()
        # 如果无路可走
        if len(monster_near_by_trees_locations) == 0:
            return
        # 循环所有位置
        for location in monster_near_by_trees_locations:
            # 推树，并返回新的地图
            new_map, new_monster_location, is_move = play_controller.monster_push_tree(location)
            if not is_move:  # 如果没有任何移动
                return
            Log.map(new_map)
            # 然后根据新的地图，继续玩，并增加递归次数
            self._play(new_map, play_count + 1, new_monster_location)

    def _find_start_location(self):
        y = 0
        for line in self.map:
            x = 0
            for value in line:
                if value == Map.start:
                    self.start_location.x = x
                    self.start_location.y = y
                    self.start_location.location_value = value
                x += 1
            y += 1

    def _find_end_location(self):
        self._find_first_location(
            [
                Map.end_double,
                Map.end_horizontal,
                Map.end_vertical
            ],
            self.end_locations
        )

    def _find_first_location(self, enum_map_types, point):
        y = 0
        for line in self.map:
            x = 0
            for value in line:
                for map_type in enum_map_types:
                    if value == map_type:
                        location = Location(x, y)
                        location.location_value = value
                        point.append(location)
                x += 1
            y += 1
