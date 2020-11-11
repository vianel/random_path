import random
class Drunk:

    def __init__(self, name):
        self.name = name

class NormalDrunk(Drunk):

    def __init__(self, name):
        super().__init__(name)

    def move(self):
       return random.choice([(0,1), (0, -1), (1,0), (-1, 0)])
