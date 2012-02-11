from Battle.Attack.EffectDelegates.charge_delegate import ChargeDelegate
from Battle.dodge import Dodge

class DodgeDelegate(ChargeDelegate):
    """ Represents an attack that dodges one turn and then attacks the next """
    
    def __init__(self, dodgeType, message):
        """ Builds a ChanceDelegate """
        self.turns = 2
        self.turnToAttack = 1
        self.message = message
        
        self.turnOn = 0
        self.dodgeType = dodgeType
        
        self.applyOnMiss = True
    
    def applyEffect(self, user, target):
        """ Applies the delegate's effect when the attack hits """
        user.dodge = None
        return []
    
    def isCharging(self, user):
        """ States when the attack is in the charging state """
        user.dodge = self.dodgeType
        return super(DodgeDelegate, self).isCharging(user)