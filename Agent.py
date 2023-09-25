import random
from Ambient import Ambient
from size import size
class Agent():
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
        choice = None
        while(choice == None):
            self.percepts = self.ambient.percepts()
            if(self.percepts.__contains__("dirty")):
                choice = "asp"
                break
            choice =  random.choice(self.choices)
            canDo = True
            if(self.percepts.__contains__("clean") and choice == "asp"):
                canDo = False
            if(self.allChoices.__len__()>0):
                previousChoice = self.allChoices[self.allChoices.__len__()-1][0]
                if((previousChoice == "left" and choice == "right")
                or (previousChoice == "right" and choice == "left")
                or (previousChoice == "up" and choice == "down")
                or (previousChoice == "down" and choice == "up")):
                    canDo = False
            for percept in self.percepts:
                if(self.restrictions.__contains__((choice, percept))):
                    canDo = False
                    choice = None
                if(choice == "noOp" and not self.ambient.cleaned()):
                    choice = None
        if(choice != "noOp" and choice != "asp"):
            if(choice == "left"): self.pos[1] -= 1
            elif(choice == "right"): self.pos[1] += 1
            elif(choice == "up"): self.pos[0] -= 1
            elif(choice == "down"): self.pos[0] += 1
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
        self.points+=self.ambient.action(choice)
        self.allChoices.append((choice, self.pos))
        self.points -= 1
        if(self.ambient.cleaned()):
            return "End"
        return "Continue"
