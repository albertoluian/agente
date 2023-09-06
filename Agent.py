import random
from Ambient import Ambient
class Agent():
    def __init__(self, choices, percepts, restrictions):
        self.choices = choices
        self.percepts = percepts
        self.restrictions = restrictions
        self.allChoices = []
        self.pos = [random.randint(0, 9), random.randint(0, 9)]
        self.points = 0
        self.ambient = Ambient(10)
    def generateChoice(self):
        choice = None
        while(choice == None):
            choice =  random.choice(self.choices)
            canDo = True
            self.percepts = self.ambient.percepts(self.pos)
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
