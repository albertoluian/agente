from Agent import Agent
import copy
import os
import numpy as np
from time import sleep
from threading import Thread
maxEncountered = []
n_threads = 16
def runAgent(n):
    global maxEncountered
    points = []
    for i in range(n):
        agent = Agent(choices=["noOp", "left", "right", "up", "down", "asp"], percepts=None, restrictions=[("left", "wallLeft"), ("right", "wallRight"), ("down", "wallDown"), ("up", "wallUp"), ("asp", "clean")])

        move = ""
        count = 1
        while(move != "End"):
            move = agent.generateChoice()
            ambient = np.asarray(copy.deepcopy(agent.ambient.ambient), dtype=object)
            ambient[agent.ambient.agentPos[0], agent.ambient.agentPos[1]] = "x"
            
            os.system('cls')
            print(ambient, "\n", "agent perception: "+str((agent.size[0]+1, agent.size[1]+1)), "\n Action"+str(agent.allChoices[agent.allChoices.__len__()-1]))
        print("This agent points: "+str(agent.points))
        points.append(agent.points)
        # print("i = "+str(i))
    maxEncountered.append(max(points))
# running 100 agents in 'n' threads
# for i in range(25):
#     print(i)
#     threads = []
#     for i in range(n_threads):
#         threads.append(Thread(target=runAgent, args=[100]))
#     for i in range(n_threads):
#         threads[i].start()
#     for i in range(n_threads):
#         threads[i].join()
runAgent(10) #agents quantity
print(max(maxEncountered))