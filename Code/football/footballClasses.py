#Matthew Vandeberg
#Python
#Period 2

class player():
    #Initialize player object and assign parameters to private variables
    def __init__(self, team, name, number):
        self.__team = team
        self.__name = name
        self.__number = number

    #Function to get the basic info of a player object
    def playerInfo(self):
        return('Team: ' + self.__team + '\nName: ' + self.__name + '\nNumber: ' + self.__number)

#footballPlayer class inherits from player class
class footballPlayer(player):
    #Calls init function of parent class and assigns other parameters to "private" variables
    def __init__(self, team, name, number, games, points):
        player.__init__(self, team, name, number)
        self._games = games
        self._points = points
    
    def activity(self):
        return 'I play football'

#quarterBack class inherits from footballPlayer class
class quarterBack(footballPlayer):
    #Calls init function of parent class and assigns other parameters to private variables
    def __init__(self, team, name, number, games, points, passYards):
        footballPlayer.__init__(self, team, name, number, games, points)
        self.__passYards = passYards

    #Overrides parent function and adds a string to the original activity string
    def activity(self):
        return footballPlayer.activity(self) + ' and I throw the rock'
    
    #Returns number of passing yards per game
    def yardsGame(self):
        return self.__passYards / self._games

    #Returns number of points scored per game
    def pointsGame(self):
        return self._points / self._games

#receiver class inherits from footballPlayer class
class receiver(footballPlayer):
    #Calls init function of parent class and assigns other parameters to private variables
    def __init__(self, team, name, number, games, points, receiveYards):
        footballPlayer.__init__(self, team, name, number, games, points)
        self.__receiveYards = receiveYards

    #Overrides parent function and adds a string to the original activity string
    def activity(self):
        return footballPlayer.activity(self) + ' and I catch the rock'

    #Returns number of receiving yards per game
    def receivingYardsGame(self):
        return self.__receiveYards / self._games

    #Returns number of points scored per game
    def pointsGame(self):
        return self._points / self._games

#runningBack class inherits from footballPlayer class
class runningBack(footballPlayer):
    #Calls init function of parent class and assigns other parameters to private variables
    def __init__(self, team, name, number, games, points, runYards):
        footballPlayer.__init__(self, team, name, number, games, points)
        self.__runYards = runYards

    #Overrides parent function and adds a string to the original activity string
    def activity(self):
        return footballPlayer.activity(self) + ' and I carry the rock'
    
    #Returns number of running yards per game
    def runningYardsGame(self):
        return self.__runYards / self._games

    #Returns number of points scored per game
    def pointsGame(self):
        return self._points / self._games