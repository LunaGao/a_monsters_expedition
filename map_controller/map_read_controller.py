from map_enum import Map


class MapReadController:

    @staticmethod
    def read_map_config_file(config_file_path):
        line_map = MapReadController.__convert_file_to_line_map(config_file_path)
        map = MapReadController.__line_map_to_map(line_map)
        map = MapReadController.__resize_map(map)
        enum_map = MapReadController.__convert_map_to_enum_map(map)
        return enum_map

    @staticmethod
    def __convert_map_to_enum_map(map):
        values = []
        for line in map:
            value = []
            for number in line:
                value.append(Map(number))
            if value:
                values.append(value)
        return values

    @staticmethod
    def __resize_map(initial_map):
        map = []
        MapReadController.__add_two_empty_lines(map, initial_map)
        for line in initial_map:
            MapReadController.__add_left_and_right_two_empty_value(map, line)
        MapReadController.__add_two_empty_lines(map, initial_map)
        return map

    @staticmethod
    def __add_left_and_right_two_empty_value(map, initial_line):
        line = [0, 0] + initial_line + [0, 0]
        map.append(line)

    @staticmethod
    def __add_two_empty_lines(map, initial_map):
        map.append(MapReadController.__add_empty_line(len(initial_map[0])))
        map.append(MapReadController.__add_empty_line(len(initial_map[0])))

    @staticmethod
    def __add_empty_line(initial_length):
        length = initial_length + 4
        empty_line = []
        while length != 0:
            empty_line.append(0)
            length -= 1
        return empty_line

    @staticmethod
    def __line_map_to_map(line_map):
        map = []
        for line in line_map:
            line_values = MapReadController.__convert_line_to_values(line)
            map.append(line_values)
        return map

    @staticmethod
    def __convert_line_to_values(line):
        values = []
        for value in line.split(','):
            values.append(int(value))
        return values

    @staticmethod
    def __convert_file_to_line_map(config_file_path):
        map = []
        with open(config_file_path, 'r') as f:
            line = MapReadController.__read_line(f, map)
            while line != '':
                line = MapReadController.__read_line(f, map)
        return map

    @staticmethod
    def __read_line(f, map):
        line = f.readline().replace('\n', '')
        if line != '':
            map.append(line)
        return line
