#Importamos as bibliotecas e arquivos necessários
import random
from Ambient import Ambient
from size import size

class Agent():
    #A classe do agente é iniciada com informações sobre as escolhas,
     #percepções, restrições, posição do agente a partir de sua percepção,
     #tamanho do ambiente que o agente percebeu, pontuação e o ambiente em si
    def __init__(self, choices, percepts, restrictions):
        self.choices = choices
        self.percepts = percepts
        self.restrictions = restrictions
        self.allChoices = []
        self.pos = [0, 0]
        self.size = [0, 0]
        self.points = 0
        self.ambient = Ambient(size)

    def generateChoice(self):
        #Aqui definimos uma lógica para a geração de escolhas, onde
         #o agente permanecerá em um loop equanto a escolha for nula
        choice = None
        while(choice == None):
            self.percepts = self.ambient.percepts()
            #O agente percebe o ambiente e então escolhe aspirar caso
             #o mesmo esteja sujo (dirty)
            if(self.percepts.__contains__("dirty")):
                choice = "asp"
                break
            #Caso o ambiente não esteja sujo, o agente irá escolher uma ação aleatória
            choice =  random.choice(self.choices)
            canDo = True
            if(self.percepts.__contains__("clean") and choice == "asp"):
                #Não permite que uma região limpa seja aspirada
                canDo = False
            
            if(self.allChoices.__len__()>0):
                #Não permite que o agente volte para a posição que estava uma ação atras
                previousChoice = self.allChoices[self.allChoices.__len__()-1][0]
                if((previousChoice == "left" and choice == "right")
                or (previousChoice == "right" and choice == "left")
                or (previousChoice == "up" and choice == "down")
                or (previousChoice == "down" and choice == "up")):
                    canDo = False
            for percept in self.percepts:
                if(self.restrictions.__contains__((choice, percept))):
                    #Analisa se há restrições para as ações do agente e 
                     #faz com que a escolha seja none, para continuar no loop
                    canDo = False
                    choice = None
                if(choice == "noOp" and not self.ambient.cleaned()):
                    #Caso a ação aleatória escolhida for não operar e o ambiente
                     #não estiver limpo, a escolha retornará a none, fazendo com que 
                     #permaneça no loop
                    choice = None
        if(choice != "noOp" and choice != "asp"):
            #Determina a mudança das coordenadas percebidas para cada movimento do agente
            if(choice == "left"): self.pos[1] -= 1
            elif(choice == "right"): self.pos[1] += 1
            elif(choice == "up"): self.pos[0] -= 1
            elif(choice == "down"): self.pos[0] += 1

            #Determina a mudança do tamanho do ambiente percebido pelo agente
            if(self.pos[0]<0):
                    self.pos[0] = 0
                    self.size[0] +=1
            if(self.pos[1]<0):
                    self.pos[1] = 0
                    self.size[1] +=1
            if(self.pos[0]>self.size[0]):
                    self.size[0] = self.pos[0]
            if(self.pos[1]>self.size[1]):
                    self.size[1] = self.pos[1]
        return self.action(choice)

    def action(self, choice):
        #Determina a ação do agente com base no ambiente que ele percebe fazendo-o 
         #parar apenas quando o ambiente estiver totalmente limpo
        self.points+=self.ambient.action(choice)
        self.allChoices.append((choice, self.pos))
        self.points -= 1
        if(self.ambient.cleaned()):
            return "End"
        return "Continue"
