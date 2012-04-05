import sys

from Battle.battle_view_controller import BattleViewController
from Trainer.computer_trainer import ComputerTrainer
from Trainer.human_trainer import HumanTrainer

from Trainer.trainer_factory import TrainerFactory


def ParseArgs(args):
    """ Parse the Command Line Arguments """
    player = None
    cpu = None
    
    if not args == []:
        if len(args) >= 2:
            player = BuildPlayer(args[0], args[1])
        if len(args) >= 4:
             cpu = BuildCPU(args[2], args[3])
            
    return player, cpu
        
def GetTrainers(player, cpu):
    """  Pick the Trainer Pkmn """
    player = ChooseTrainer(player, TrainerFactory.HUMAN)
    cpu = ChooseTrainer(cpu, TrainerFactory.COMPUTER)
    return player, cpu
    
def ChooseTrainer(trainer, type):
    """ Choose a Trainer """
    while trainer == None:
        title = raw_input("Pick Trainer Title:")
        name = raw_input("Pick Trainer Name:")
        trainer = BuildTrainer(title, name, type)
    return trainer
    
def BuildPlayer(title, name):
    return BuildTrainer(title, name, TrainerFactory.HUMAN)
    
def BuildCPU(title, name):
    return BuildTrainer(title, name, TrainerFactory.COMPUTER)
    
def BuildTrainer(title, name, type):
    title = title.strip("'")
    name = name.strip("'")
    return TrainerFactory.loadFromXML(title, name, type)
    
def Battle(player, cpu):
    BattleViewController().begin(player, cpu)
    
def Loop(player, cpu):
    player, cpu = GetTrainers(player, cpu)
    Battle(player, cpu)

def main(argv):
    """ Start the game """
    player, cpu = ParseArgs(argv)
    Loop(player, cpu)

if __name__ == "__main__":
    main(sys.argv[1:])