from Battle.Weather.weather import Weather

class BattleEnvironment:
    """ Represents the Environemnt a Battle is taking place in """
    
    def __init__(self):
        """ Build the Battle Environment default """
        # Eventually, this will need to receive the tile-type
        self.weather = Weather(None)
        
    def betweenRounds(self, playerSide, opponentSide):
        """ Function to handle events Between Turns """
        return self.weather.betweenRounds(playerSide, opponentSide)