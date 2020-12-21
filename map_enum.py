from enum import Enum


class Map(Enum):
    sea = 0  # 海
    land = 1  # 陆地
    stone = 2  # 石头
    tree1 = 3  # 树（一个格的）
    tree2 = 4  # 树（两个格的）
    start = 5  # 起始点（陆地）

    stump = 10  # 树桩

    tree_stand = 20  # 单节长度 立着的 木棍
    tree_horizontal_1 = 21  # 单节长度 横着的 木棍
    tree_vertical_1 = 22  # 单节长度 竖着的 木棍
    tree_horizontal_2 = 23  # 双节长度 横着的 木棍
    tree_vertical_2 = 24  # 双节长度 竖着的 木棍
    tree_horizontal_1_sea = 25  # 单节长度 横着的 海中的 木棍
    tree_vertical_1_sea = 26  # 单节长度 竖着的 海中的 木棍
    tree_horizontal_2_sea = 27  # 双节长度 横着的 海中的 木棍
    tree_vertical_2_sea = 28  # 双节长度 竖着的 海中的 木棍

    end_horizontal = 90  # 终点（海里，横着）
    end_vertical = 91  # 终点（海里，竖着）
    end_double = 92  # 终点（海里），需要2个木桩
    end_horizontal_1 = 93  # 终点（有一个木桩在海里，横着）
    end_vertical_1 = 94  # 终点（有一个木桩在海里，竖着）
    end_double_2 = 95  # 终点（有两个木桩在海里）
