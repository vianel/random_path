class Field:

    def __init__(self):
        self.drunk_coordinates = {}

    def add_drunker(self, drunk, coordinate):
        self.drunk_coordinates[drunk] = coordinate

    def move_drunker(self, drunk):
        delta_x, delta_y = drunk.move()
        current_coordinate = self.drunk_coordinates[drunk]
        new_coordinate = current_coordinate.move(delta_x, delta_y)

        self.drunk_coordinates[drunk] = new_coordinate

    def get_coordinate(self, drunk):
        return self.drunk_coordinates[drunk]
