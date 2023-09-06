import random
from Ambient import Ambient
from size import size
class Agent():
    def __init__(self, choices, percepts, restrictions):
        self.choices = choices
        self.percepts = percepts
        self.restrictions = restrictions
        self.allChoices = []
        self.pos = [random.randint(0, size-1), random.randint(0, size-1)]
        self.points = 0
        self.ambient = Ambient(10)
    def generateChoice(self):
        choice = None
        while(choice == None):
            self.percepts = self.ambient.percepts(self.pos)
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
        return self.action(choice)

    def action(self, choice):
        if(choice == "left"): self.pos[1] -= 1
        elif(choice == "right"): self.pos[1] += 1
        elif(choice == "up"): self.pos[0] -= 1
        elif(choice == "down"): self.pos[0] += 1
        elif(choice == "asp"): 
            cleaned = self.ambient.clean(self.pos)
            if(cleaned): self.points += 2
        self.allChoices.append((choice, self.pos))
        self.points -= 1
        if(self.ambient.cleaned()):
            return "End"
        return "Continue"
