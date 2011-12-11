from Battle.Actions.action_factory import ActionFactory
from Battle.battle import Battle
from Screen.Console.battle_view import ConsoleBattleScreen

class BattleViewController:
    """ Controls the interaction between the visible Screen and a battle 
    between two Trainers """
    
    def __init__(self):
        """  """
        
        
    def begin(self, playerTrainer, oppTrainer):
        """ Starts showing the Battle Screen and initializes the Battle """
        self.battle = Battle(playerTrainer, oppTrainer)
        self.screen = ConsoleBattleScreen(self.battle)
        
        # Play intro (DUNANANANANANANAAAA!)
        
        
        # Introduce the Battle Environment
        self.screen.introduce()
        
        self.sendOutPkmnOnSide(self.battle.oppSide)
        self.sendOutPkmnOnSide(self.battle.playerSide)
        
        # Start the Game Loop
        #self.gameLoop()
        
    def sendOutPkmnOnSide(self, side):
        """ Sends out the Pkmn for the given side """
        messages = side.sendOutPkmn()
        for message in messages:
            self.screen.reportMessage(message)
        
    def gameLoop(self):
        """ Runs through one iteration if the game """
        while (not self.battle.over):
            # Pick action
            if self.battle.playerSide.trainer.actionLock is None:
                # Print the stats of each Pokemon
                self.screen.printScreen()
                actionParams = self.screen.pickAction()
                action = ActionFactory.buildActionFromType(actionParams)
            else:
                action = self.battle.playerSide.trainer.actionLock.useAction()
        
            # Have the Battle start the battle iteration
            sAndAs = self.battle.battle(action)
        
            for i in range(2):
                messages = self.battle.act(sAndAs[i].side, sAndAs[i].action, sAndAs[not i].side)
                if self.reportAndCheckEnd(messages):
                    return
                
                messages = self.battle.afterTurn(sAndAs[i].side, self.reportAndCheckEnd,\
                                                                sAndAs[not i].side)
                if self.reportAndCheckEnd(messages):
                    return
                
                self.battle.betweenTurns(self.reportAndCheckEnd)
                if self.checkOver():
                    return
                    
    def reportAndCheckEnd(self, messages):
        """ Report the messages given and check if the game is over """
        if messages:
            self.screen.reportAction(messages)
            self.screen.reportAction(self.battle.checkFaint())
        
        return self.checkOver()
        
    def checkOver(self):
        """ Checks if the Battle is over """
        return self.battle.over