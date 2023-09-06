from Agent import Agent
import copy
import os
agent = Agent(choices=["noOp", "left", "right", "up", "down", "asp"], percepts=None, restrictions=[("left", "wallLeft"), ("right", "wallRight"), ("down", "wallDown"), ("up", "wallUp"), ("asp", "clean")])

move = ""
count = 1
while(move != "End"):
    move = agent.generateChoice()
    ambient = copy.deepcopy(agent.ambient.ambient)
    ambient[agent.pos[0], agent.pos[1]] = 2
    os.system('cls')
    print(ambient, agent.allChoices[agent.allChoices.__len__()-1])
print(agent.points)
