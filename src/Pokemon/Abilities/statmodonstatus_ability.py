from ability import Ability

class StatModOnStatusAbility(Ability):
    """ An ability that modifies a stat when the parent receives a status """
    
    def __init__(self, name, status, stat, mod):
        """ Builds the Ability """
        self.name = name
        self.status = status
        self.stat = stat
        self.mod = mod
        
    def onStatus(self, side, status):
        """ Alter the statMods of the Status to reflect the abilities effect """
        status.statMods[self.stat] = self.mod
        return [side.getHeader() + " raised it's " + self.stat + "."]