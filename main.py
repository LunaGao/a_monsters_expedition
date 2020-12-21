from map_controller.game_controller import GameController
from map_controller.map_read_controller import MapReadController
from program_helper.print_helper import Log

# 1. 读取map.config中的文件
enum_map = MapReadController.read_map_config_file('map.config')
Log.map(enum_map)
# 2. 玩游戏
deep_count = 10
gameController = GameController(enum_map)
gameController.play_game(deep_count)
