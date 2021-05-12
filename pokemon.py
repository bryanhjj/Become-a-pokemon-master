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
        return "The pokemon {name} is at level{level} with {curHp}/{maxHp} HP remaining.".format(name = self.name, level = self.level, curHp = self.curHp, maxHp = self.maxHp)
    
    def is_Knocked_Out(self):
        #a function that switches a pokemons' KO status to true when hp reaches 0
        if (self.curHp == 0) :
            print("{name} is knocked out and unable to battle!".format(name = self.name))
            return self.knockedOut == True
    
    def take_Damage(self, damageTaken):
        #function for when a pokemon receives damage
        self.curHp -= damageTaken
        #if damage taken exceeds remaining hp
        if (self.curHp < 0):
            self.curHp = 0
        print("{name} has {curHp} HP remaining!".format(name = self.name, curHp = self.curHp))
        self.is_Knocked_Out()
    
    def recover_Health(self, healthRecovered):
        #function for when a healing item/move is used on a pokemon
        self.curHp += healthRecovered
        if (self.curHp > self.maxHp):
            self.curHp = self.maxHp
        print("{name} has regained some hp and now has {curHp} HP remaining!".format(name = self.name, curHp = self.curHp))

    def type_Check(self, targetPokemon):
        #check for type advantage and return the appropriate damage modifier
        if (self.type == "grass" and targetPokemon.type == "grass"):
            print ("It's not very effective...")
            return 0.5
        elif (self.type == "grass" and targetPokemon.type == "fire"):
            print ("It's not very effective...")
            return 0.5
        elif (self.type == "grass" and targetPokemon.type == "water"):
            print ("It's super effective!")
            return 2
        elif (self.type == "fire" and targetPokemon.type == "fire"):
            print ("It's not very effective...")
            return 0.5
        elif (self.type == "fire" and targetPokemon.type == "water"):
            print ("It's not very effective...")
            return 0.5
        elif (self.type == "fire" and targetPokemon.type == "grass"):
            print ("It's super effective!")
            return 2
        elif (self.type == "water" and targetPokemon.type == "water"):
            print ("It's not very effective...")
            return 0.5
        elif (self.type == "water" and targetPokemon.type == "fire"):
            print ("It's super effective!")
            return 2
        elif (self.type == "water" and targetPokemon.type == "grass"):
            print ("It's not very effective...")
            return 0.5
        else:
            return 1
    
    def attack(self, attackValue, targetPokemon):
        #function for attacking another players' pokemon
        targetPokemon.take_Damage((attackValue * self.type_Check(targetPokemon)))
    
    def revive(self):
        #a function to revive fainted/KO'd pokemon back to fighting condition
        self.knockedOut == False
        print("{name} has recovered from fainting!")


#create trainer class
class Trainer:
    def __init__(self) -> None:
        pass


    

        