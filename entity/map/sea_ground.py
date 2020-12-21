from entity.map.base_ground import BaseGround


class SeaGround(BaseGround):
    
    def __init__(self):
        super().__init__()
        self.canStand = False
