from entity.Location import Location
from map_enum import Map


class RoadController:

    def __init__(self, map, start_point, end_point, arrived_map=None):
        if arrived_map is None:
            arrived_map = []
        self.map = map
        self.start_point = start_point
        self.end_point = end_point
        self.arrived_map = arrived_map
        self._create_arrived_map()

    def is_arrived(self):
        next_locations = self._find_all_next_locations()
        if len(next_locations) == 0:
            return False
        for next_location in next_locations:
            if next_location.x == self.end_point.x and next_location.y == self.end_point.y:
                return True
            road_controller = RoadController(self.map, next_location, self.end_point, self.arrived_map)
            if road_controller.is_arrived():
                return True
        return False

    def _find_all_next_locations(self):
        all_next_locations = []
        x = self.start_point.x
        y = self.start_point.y
        locations = [
            Location(x-1, y, self.map[y][x-1]),  # 左边的
            Location(x+1, y, self.map[y][x+1]),  # 右边的
            Location(x, y-1, self.map[y-1][x]),  # 上边的
            Location(x, y+1, self.map[y+1][x]),  # 下边的
        ]
        for location in locations:
            map_type = self.map[location.y][location.x]
            # 如果没有到达过
            if self.arrived_map[location.y][location.x] == 0:
                if map_type == Map.land:  # 如果是在陆地上
                    self._add_next_location(all_next_locations, location)
                if map_type == Map.stump:  # 如果是在树桩上
                    self._add_next_location(all_next_locations, location)
                if map_type == Map.tree_horizontal_1_sea:  # 单节长度 横着的 海中的 木棍
                    self._add_next_location(all_next_locations, location)
                if map_type == Map.tree_vertical_1_sea:  # 单节长度 竖着的 海中的 木棍
                    self._add_next_location(all_next_locations, location)
                if map_type == Map.tree_horizontal_2_sea:  # 双节长度 横着的 海中的 木棍
                    self._add_next_location(all_next_locations, location)
                if map_type == Map.tree_vertical_2_sea:  # 双节长度 竖着的 海中的 木棍
                    self._add_next_location(all_next_locations, location)
        return all_next_locations

    def _add_next_location(self, all_next_locations, location):
        all_next_locations.append(location)
        self.arrived_map[location.y][location.x] = 1

    def _create_arrived_map(self):
        if not self.arrived_map:
            x_count = len(self.map)
            y_count = len(self.map[0])
            self.arrived_map = []
            for x in range(x_count):
                line = []
                for y in range(y_count):
                    line.append(0)
                self.arrived_map.append(line)
