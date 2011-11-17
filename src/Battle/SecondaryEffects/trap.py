from secondary_effect import SecondaryEffect

import random

class Trap(SecondaryEffect):
    """ Represents a Trap effect on a Pokemon """
    minTurns = 4
    ratio = 16
    
    def __init__(self, message, doneMessage):
        """ Builds a trap with the given message """
        self.message = message
        self.doneMessage = doneMessage
        self.turns = self.getTurns()
        
    def getTurns(self):
        """ Returns the 4-5 turns """
        return Trap.minTurns + random.randint(0, 1)
        
    def afterTurn(self, side):
        """ Does the damage of the Trap """
        user = side.currPokemon
        self.damage(user)
        
        messages = [side.getHeader() + self.message]
        self.turns = self.turns - 1
        
        if self.turns == 0:
            side.secondaryEffects.remove(self)
            messages.append(side.getHeader() + self.doneMessage)
        
        return messages
        
    def damage(self, user):
        """ Damages the user """
        user.takeDamage(self.getDamage(user))
        
    def getDamage(self, user):
        """ Returns the damage the Trap causes """
        return user.getRatioOfHealth(Trap.ratio)