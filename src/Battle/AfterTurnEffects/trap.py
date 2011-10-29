import random

class Trap:
    """ Represents a Trap effect on a Pokemon """
    minTurns = 4
    ratio = 16
    
    def __init__(self, message):
        """ Builds a trap with the given message """
        self.message = message
        self.turns = self.getTurns()
        
    def getTurns(self):
        """ Returns the 4-5 turns """
        return Trap.minTurns + random.randint(0, 1)
        
    def afterTurn(self, side):
        """ Does the damage of the Trap """
        user = side.currPokemon
        self.damage(user)
        
        message = side.getHeader() + self.message
        self.turns = self.turns - 1
        return [message]
        
    def damage(self, user):
        """ Damages the user """
        user.takeDamage(self.getDamage(user))
        
    def getDamage(self, user):
        """ Returns the damage the Trap causes """
        return user.getRatioOfHealth(Trap.ratio)