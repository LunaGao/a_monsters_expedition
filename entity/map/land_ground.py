from entity.map.base_ground import BaseGround


class LandGround(BaseGround):
    def __init__(self):
        super().__init__()
        self.canStand = True
