from map_enum import Map


class Log:
    @staticmethod
    def map(map):
        print("---------map---------")
        for line in map:
            line_str = ''
            for location in line:
                value = '❓'
                if location == Map.sea:
                    value = '🌊'
                if location == Map.land:
                    value = '🍃'
                if location == Map.stone:
                    value = '🍞'
                if location == Map.tree1:
                    value = '🌲'
                if location == Map.tree2:
                    value = '🌴'
                if location == Map.start:
                    value = '🚀'
                if location == Map.end_horizontal:
                    value = '😀'
                if location == Map.stump:
                    value = '🌱'
                if location == Map.tree_horizontal_1:
                    value = '👉'
                if location == Map.tree_vertical_1:
                    value = '👆'
                if location == Map.tree_horizontal_1_sea:
                    value = '🚣'
                if location == Map.tree_vertical_1_sea:
                    value = '⛵'
                line_str += value
            print(line_str)

    @staticmethod
    def monster(monster):
        print("-------monster-------")
        print(monster.to_string())

    @staticmethod
    def monsters(monsters):
        print("------monsters-------")
        for monster in monsters:
            print(monster.to_string())

    @staticmethod
    def location(location):
        print("------location-------")
        print(location.to_string())

    @staticmethod
    def locations(locations):
        print("------location-------")
        for location in locations:
            print(location.to_string())

    @staticmethod
    def trees(trees):
        print("--------trees--------")
        for tree in trees:
            print(tree.to_string())
