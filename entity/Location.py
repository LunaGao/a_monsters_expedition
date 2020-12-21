from push_enum import Push


class Location:
    x = 0
    y = 0
    location_value = None
    push_location = None

    def __init__(self, x, y, location_value=None, push_location=None):
        self.x = x
        self.y = y
        self.location_value = location_value
        self.push_location = push_location

    def set_location_value(self, location_value):
        self.location_value = location_value

    def to_string(self):
        return 'x:' + str(self.x) + ' y:' + str(self.y) + ' location value: ' + str(self.location_value) + \
               ' push value: ' + str(self.push_location)
