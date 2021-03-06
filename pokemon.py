#create a pokemon class with some basic functionalities
class Pokemon:
    def __init__(self, name, type, maxHp, curHp, level = 5, knockedOut=False):
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
            return 0.5
        elif (self.type == "grass" and targetPokemon.type == "fire"):
            return 0.5
        elif (self.type == "grass" and targetPokemon.type == "water"):
            return 2
        elif (self.type == "fire" and targetPokemon.type == "fire"):
            return 0.5
        elif (self.type == "fire" and targetPokemon.type == "water"):
            return 0.5
        elif (self.type == "fire" and targetPokemon.type == "grass"):
            return 2
        elif (self.type == "water" and targetPokemon.type == "water"):
            return 0.5
        elif (self.type == "water" and targetPokemon.type == "fire"):
            return 2
        elif (self.type == "water" and targetPokemon.type == "grass"):
            return 0.5
        else:
            return 1
    
    def attack(self, targetPokemon):
        #function for attacking another players' pokemon
        print("{name} attacks {targetName}!".format(name = self.name, targetName = targetPokemon.name))
        if (self.type == "grass" and targetPokemon.type == "grass"):
            print ("It's not very effective...")
        elif (self.type == "grass" and targetPokemon.type == "fire"):
            print ("It's not very effective...")
        elif (self.type == "grass" and targetPokemon.type == "water"):
            print ("It's super effective!")
        elif (self.type == "fire" and targetPokemon.type == "fire"):
            print ("It's not very effective...")
        elif (self.type == "fire" and targetPokemon.type == "water"):
            print ("It's not very effective...")
        elif (self.type == "fire" and targetPokemon.type == "grass"):
            print ("It's super effective!")
        elif (self.type == "water" and targetPokemon.type == "water"):
            print ("It's not very effective...")
        elif (self.type == "water" and targetPokemon.type == "fire"):
            print ("It's super effective!")
        elif (self.type == "water" and targetPokemon.type == "grass"):
            print ("It's not very effective...")
        else:
            return
        targetPokemon.take_Damage((self.level * self.type_Check(targetPokemon)))
        print("{name} has dealt {damage} damage to {targetName}!".format(name = self.name, damage = round(self.level * self.type_Check(targetPokemon)), targetName = targetPokemon.name))
    
    def revive(self):
        #a function to revive fainted/KO'd pokemon back to fighting condition
        self.knockedOut == False
        print("{name} has recovered from fainting!".format(name = self.name))



#create trainer class
class Trainer:
    def __init__(self, name, listOfPokemon):
        #providing trainers with a default of 3 potions and 1 revives for use
        self.name = name
        self.numPotions = 3
        self.numRevives = 1
        self.pokemons = listOfPokemon
        self.curPokemon = self.pokemons[0]

    def __repr__(self):
        #a quick description of the trainer
        return "Trainer {name} has {potions} potions and {revives} revives left.".format(name = self.name, potions = self.numPotions, revives = self.numRevives)
    
    def use_Potion(self):
        #function to allow players to use potion on their pokemon
        if (self.numPotions <= 0):
            self.numPotions = 0
            print("You do not have any potions left to use!")
        else:
            self.numPotions -= 1
            print("You used a potion on {pokemonName}.".format(pokemonName = self.curPokemon.name))
            self.curPokemon.recover_Health(20)

    def use_Revive(self, choiceOfPokemon = 0):
        #similar to the use_Potion fuction, this allows players to revive a pokemon from fainting and allows them to bring it back into battle
        if (self.numRevives <= 0):
            self.numRevives = 0
            print("You do not have any revives left to use!")
        else:
            self.numRevives -= 1
            print("You used a revive on {pokemonName}.".format(pokemonName = self.pokemons[choiceOfPokemon].name))
            self.pokemons[choiceOfPokemon].revive()
    
    def switch_Pokemon(self, newActive):
        #a function that allows players to switch out current active pokemon
        if (newActive < len(self.pokemons) and newActive >= 0):
            if (newActive == self.curPokemon):
                print("{name} is already your current active pokemon!".format(name = self.curPokemon.name))
            elif (self.pokemons[newActive].knockedOut == True):
                print("{name} has already fainted and is unable to battle.".format(self.poekmons[newActive].name))
            else:
                self.curPokemon = self.pokemons[newActive]
                print("Go {name}! You got this!".format(name = self.pokemons[newActive].name))
    
    def attack_Another_Dude(self, otherTrainer):
        #the trainer orders their pokemon to attack the other trainers' active pokemon
        targetPokemon = otherTrainer.curPokemon
        self.curPokemon.attack(targetPokemon)



#Creating some pokemons and trainers for testing
class Cyndaquil(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Cyndaquil", "fire", 39, 39, level)

class Piplup(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Piplup", "water", 53, 53, level)

class Snivy(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Snivy", "grass", 45, 45, level)

class Eevee(Pokemon):
    #added a normal type pokemon to test for neutral effective attacks
    def __init__(self, level = 5):
        super().__init__("Eevee", "normal", 55, 55, level)

pk1 = Cyndaquil(7)
pk2 = Piplup(7)
pk3 = Snivy(7)
pk4 = Eevee(7)

trainer1 = Trainer("Bryan", [pk1, pk2])
trainer2 = Trainer("Brandon", [pk3, pk4])

#print(trainer1)
#print(trainer2)
#print(pk1)

#testing the functions:
#test 1) trainer attacking another trainer with a super effective move
#trainer1.attack_Another_Dude(trainer2)

#test 2) trainer attacking with a not so effective move
#trainer2.attack_Another_Dude(trainer1)

#test 3) switching pokemon and attacking with a neutrally effective move
#trainer2.switch_Pokemon(1)
#trainer2.attack_Another_Dude(trainer1)
#test 4) trainer1 using a potion on their pokemon after receiving damage from trainer2s' pokemon
#trainer1.use_Potion()

#test 5) testing the KO function
#trainer1.attack_Another_Dude(trainer2)
#trainer1.attack_Another_Dude(trainer2)
#trainer1.attack_Another_Dude(trainer2)
#trainer1.attack_Another_Dude(trainer2)
#test 6) testing revive function (trainer2 revives snivy after the onslaught)
#trainer2.use_Revive()