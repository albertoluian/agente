#Importamos as bibliotecas e arquivos necessários
import numpy as np
from size import size
import random


class Ambient():
    #A classe Ambient cria um ambiente com tamanho sizer e, em 
     #cada posição da matriz ambiente, determina um valor que varia
     #entre 0 e 1, onde 1 quer dizer sujo e 0 limpo
    def __init__(self, size):
        self.ambient = np.random.randint(0, 2, (size, size), dtype=int)
        self.agentPos = [random.randint(0, size-1), random.randint(0, size-1)]

    def action(self, action):
        #Determina a pontuação positiva ao aspirar um local sujo e zera a mesma
         #caso o local já esteja limpo
        points = 0
        if(action == "asp"):
            if(self.ambient[self.agentPos[0], self.agentPos[1]] == 0):
                points = 0
            else: 
                self.ambient[self.agentPos[0], self.agentPos[1]] = 0
                points = 2
        
        #Muda a posição do agente dentro do ambiente, conforme o agente se movimenta
         #diminuindo em 1 a pontuação a cada ação de movimento
        elif(action == "left"): self.agentPos[1] -= 1
        elif(action == "right"): self.agentPos[1] += 1
        elif(action == "up"): self.agentPos[0] -= 1
        elif(action == "down"): self.agentPos[0] += 1
        points -=1
        return points
    def percepts(self):
        #Permite que o agente perceba que está nas bordas da matriz, se o local está sujo
         #ou se o local está limpo
        percept = []
        if(self.agentPos[0] == 0):
            percept.append("wallUp")
        if(self.agentPos[1] == 0):
            percept.append("wallLeft")
        if(self.agentPos[0] == len(self.ambient) - 1):
            percept.append("wallDown")
        if(self.agentPos[1] == len(self.ambient) - 1):
            percept.append("wallRight")
        if(self.ambient[self.agentPos[0], self.agentPos[1]] == 1):
            percept.append("dirty")
        else:
            percept.append("clean")
        return percept
    def cleaned(self):
        #Encerra as ações do agente caso o ambiente esteja completamente limpo
        if(np.array_equal(self.ambient, np.zeros(self.ambient.shape, dtype=int))):
            return True
        return False
