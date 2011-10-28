from Battle.Attack.DamageDelegates.statratio_delegate import StatRatioDelegate

from Battle.battle_side import BattleSide
from Trainer.trainer import Trainer
from Pokemon.pokemon import Pokemon

import unittest

class getPower(unittest.TestCase):
    """ Test that core damage is calculated correctly """ 
    
    def setUp(self):
        """ Setup the attack and Pokemon to use the attack """
        trainer = Trainer()
        self.user = Pokemon("BULBASAUR")
        trainer.beltPokemon = [self.user]
        self.actingSide = BattleSide(trainer)
        
        trainer2 = Trainer()
        self.target = Pokemon("BULBASAUR")
        trainer2.beltPokemon = [self.target]
        self.otherSide = BattleSide(trainer2)
        
        self.stat = "SPD"
        
        self.delegate = StatRatioDelegate(None, 1, self.stat)
        
    def basePower(self):
        """ Test that the base power is correct """
        self.user.battleDelegate.stats[self.stat] = 25
        self.target.battleDelegate.stats[self.stat] = 25
        power = self.delegate.getPower(self.actingSide, self.otherSide)
        
        assert power == StatRatioDelegate.base, "Power should be the base when the ratio of the stat is 0"
        
    def powerIsLarger(self):
        """ Test that the power is greater when the user's stat is lower """
        self.user.battleDelegate.stats[self.stat] = 20
        self.target.battleDelegate.stats[self.stat] = 25
        power = self.delegate.getPower(self.actingSide, self.otherSide)
        
        assert power > StatRatioDelegate.base, "Power should be larger when user's stat decreases"
        
    def powerIsSmaller(self):
        """ Test that the power is smaller when the user's stat is higher """
        self.user.battleDelegate.stats[self.stat] = 30
        self.target.battleDelegate.stats[self.stat] = 25
        power = self.delegate.getPower(self.actingSide, self.otherSide)
        
        assert power < StatRatioDelegate.base, "Power should be smaller when user's stat increases"
        
    def powerIsMax(self):
        """ Test that the power is not greater than the max """
        self.user.battleDelegate.stats[self.stat] = 1
        self.target.battleDelegate.stats[self.stat] = 300
        power = self.delegate.getPower(self.actingSide, self.otherSide)
        
        assert power ==  StatRatioDelegate.max, "Power should be max at greatest"


# Collect all test cases in this class      
testcasesGetPower = ["basePower", "powerIsLarger", "powerIsSmaller", "powerIsMax"]
suiteGetPower = unittest.TestSuite(map(getPower, testcasesGetPower))

#########################################################

suites = [suiteGetPower]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()