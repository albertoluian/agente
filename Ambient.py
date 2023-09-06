import numpy as np
from size import size
class Ambient():
    def __init__(self, size):
        self.ambient = np.random.randint(0, 2, (size, size), dtype=int)

    def clean(self, pos):
        if(self.ambient[pos[0], pos[1]] == 0):
            return False
        else: 
            self.ambient[pos[0], pos[1]] = 0
            return True
    def percepts(self, pos):
        percept = []
        if(pos[0] == 0):
            percept.append("wallUp")
        if(pos[1] == 0):
            percept.append("wallLeft")
        if(pos[0] == len(self.ambient) - 1):
            percept.append("wallDown")
        if(pos[1] == len(self.ambient) - 1):
            percept.append("wallRight")
        if(self.ambient[pos[0], pos[1]] == 1):
            percept.append("dirty")
        else:
            percept.append("clean")
        return percept
    def cleaned(self):
        if(np.array_equal(self.ambient, np.zeros(self.ambient.shape, dtype=int))):
            return True
        return False

