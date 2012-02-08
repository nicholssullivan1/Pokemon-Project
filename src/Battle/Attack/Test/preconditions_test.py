import unittest
from Test.test_helper import BuildPokemonBattleWrapper, BuildActionLock

from Battle.Attack.attackfactory import AttackFactory
from Battle.Attack.preconditions import PreconditionChecker

class checkLock(unittest.TestCase):
    """ Test cases of checkLock """
    
    def  setUp(self):
        """ Build the Pkmn, Lock, and Precondition Checker for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        self.actionLock = BuildActionLock(user = self.user)
        attack = AttackFactory.getAttackAsNew("TACKLE")
        self.preconditionChecker = PreconditionChecker(self.user, self.target, attack)
        
    def hasLock(self):
        """ Test that check lock returns correctly when the user has a lock  """
        self.user.actionLock = self.actionLock
        stop, messages = self.preconditionChecker.checkLock()
        
        message = "{0} USED {1}".format(self.user.getHeader(), self.actionLock.action.attack.name)
        
        assert stop, "Should stop if the user has a lock"
        assert len(messages) > 0,  "Should receive the messages for the actual attack"
        assert messages[0] == message, "Should use the actionLock attack"
        
    def noLock(self):
        """ Test that check lock returns correctly when the user has no lock """
        self.user.actionLock = None
        stop, messages = self.preconditionChecker.checkLock()
        
        assert not stop, "Should not stop if the user has no lock"
        assert messages == [], "Should not receive any messages"
        

# Collect all test cases in this class
testcasesCheckLock = ["hasLock", "noLock"]
suiteCheckLock = unittest.TestSuite(map(checkLock, testcasesCheckLock))

##########################################################

class checkFlinch(unittest.TestCase):
    """ Test cases of checkFlinch """
    
    def  setUp(self):
        """ Build the Pkmn, Lock, and Precondition Checker for the test """
        self.user = BuildPokemonBattleWrapper()
        self.target = BuildPokemonBattleWrapper()
        
        attack = AttackFactory.getAttackAsNew("TACKLE")
        self.preconditionChecker = PreconditionChecker(self.user, self.target, attack)
        
    def flinching(self):
        """ Test that check lock returns correctly when the user has a lock  """
        self.user.flinching = True
        stop, messages = self.preconditionChecker.checkFlinch()
        
        message = [self.user.getHeader() + " flinched."]
        
        assert stop, "Should stop if the user flinches"
        assert messages == message, "Should have flinching message"
        
    def notFlinching(self):
        """ Test that check lock returns correctly when the user has no lock """
        self.user.flinching = False
        stop, messages = self.preconditionChecker.checkLock()
        
        assert not stop, "Should not stop if the user isn't flinching"
        assert messages == [], "Should not receive any messages"
        

# Collect all test cases in this class
testcasesCheckFlinch = ["flinching", "notFlinching"]
suiteCheckFlinch = unittest.TestSuite(map(checkFlinch, testcasesCheckFlinch))

##########################################################

# Collect all test cases in this file
suites = [suiteCheckLock, suiteCheckFlinch]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    unittest.main()