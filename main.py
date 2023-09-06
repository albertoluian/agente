from Agent import Agent
import copy
import os
import numpy as np
from time import sleep
agent = Agent(choices=["noOp", "left", "right", "up", "down", "asp"], percepts=None, restrictions=[("left", "wallLeft"), ("right", "wallRight"), ("down", "wallDown"), ("up", "wallUp"), ("asp", "clean")])

move = ""
count = 1
while(move != "End"):
    move = agent.generateChoice()
    ambient = np.asarray(copy.deepcopy(agent.ambient.ambient), dtype=object)

    ambient[agent.pos[0], agent.pos[1]] = "x"
    os.system('cls')
    print(ambient, agent.allChoices[agent.allChoices.__len__()-1])
    sleep(0.001)
print(agent.points)
