#Importamos as bibliotecas e arquivos necessários
from Agent import Agent
import copy
import os
import numpy as np
from time import sleep
from threading import Thread
#Cria uma lista para armazenar a pontuação de cada teste feito
maxEncountered = []

def runAgent(n):
    #Serve para rodar o código para vários agentes
    global maxEncountered
    points = []
    for i in range(n):
        #Define as escolhas e restrições do agente, juntamente com a percepção inicial
        agent = Agent(choices=["noOp", "left", "right", "up", "down", "asp"], percepts=None, restrictions=[("left", "wallLeft"), ("right", "wallRight"), ("down", "wallDown"), ("up", "wallUp"), ("asp", "clean")])

        move = ""
        while(move != "End"):
            #Determina o movimento atual e printa a escolha do agente
            move = agent.generateChoice()
            ambient = np.asarray(copy.deepcopy(agent.ambient.ambient), dtype=object)
            ambient[agent.ambient.agentPos[0], agent.ambient.agentPos[1]] = "x"
            
            os.system('cls')
            print(ambient, "\n", "agent perception: "+str((agent.size[0]+1, agent.size[1]+1)), "\n Action"+str(agent.allChoices[agent.allChoices.__len__()-1]))
        #Após o agente finalizar de limpar todo o ambiente, o código printa a pontuação 
         #total do agente e também adiciona a pontuação em "points"
        print("This agent points: "+str(agent.points))
        points.append(agent.points)
        
    maxEncountered.append(max(points))

#Roda a função 10 vezes e informa a maior pontuação encontrada, podendo
 #ser alterado para a quantidade necessária de agentes
runAgent(10)
print(max(maxEncountered))
