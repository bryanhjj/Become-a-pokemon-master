#create a pokemon class with some basic functionalities
class Pokemon:
    def __init__(self, name, level, type, maxHp, curHp, knockedOut=False):
        self.name = name
        self.level = level
        self.type = type
        self.maxHp = maxHp
        self.curHp = curHp
        self.knockedOut = knockedOut

    def __repr__(self):
        #a quick description of the pokemon
        return "The pokemon {self.name} is at level{self.level} with {self.curHp}/{self.maxHp} HP remaining."
    
    def is_Knocked_Out(self):
        #a function that switches a pokemons' KO status to true when hp reaches 0
        if (self.curHp == 0) :
            print("{self.name} is knocked out and unable to battle!")
            return self.knockedOut == True
    
    def take_Damage(self, damageTaken):
        #function for when a pokemon receives damage
        self.curHp -= damageTaken
        #if damage taken exceeds remaining hp
        if (self.curHp < 0):
            self.curHp = 0
        print("{self.name} has {self.curHp} HP remaining!")
        self.is_Knocked_Out()
    
    def recover_Health(self, healthRecovered):
        #function for when a healing item/move is used on a pokemon
        self.curHp += healthRecovered
        if (self.curHp > self.maxHp):
            self.curHp = self.maxHp
        print("{self.name} has regained some hp and now has {self.curHp} HP remaining!")
            

