#----------------- Created a Player class ---------------------
class Player:
    ''' static variables '''
    TOTAL_SCORE = 0
    TOTAL_OUT = 0
    EXTRAS = 0

    ''' parameterized constructor created '''
    def __init__(self,playerName,scores=0,fourRuns=0,sixRuns=0,balls=0,stillBatting = False, out = False):
        self.__playerName = playerName
        if stillBatting:
            self.__playerName = playerName+'*'
        self.__scores = scores
        self.__balls = balls
        self.__fourRuns = fourRuns
        self.__sixRuns = sixRuns
        self.__stillBatting = stillBatting
        self.__out = out
        Player.TOTAL_SCORE = Player.TOTAL_SCORE + scores
        if out:
            Player.TOTAL_OUT +=1


    @staticmethod
    def addScore(score = 1):
        ''' static method to take score as input and add 
            to the team scores (TOTAL_SCORE) and 
            also adding if any extras (EXTRAS) 
        '''

        num = Player.TOTAL_SCORE
        Player.TOTAL_SCORE = num + score
        Player.EXTRAS +=1

    @staticmethod
    def resetVar():
        ''' static method When the 2nd Team play then reset 
            the values of all the static variables 
        '''

        Player.TOTAL_SCORE = 0
        Player.EXTRAS = 0
        Player.TOTAL_OUT = 0


    def setScores(self,scores):
        ''' take the scores and set the total score (TOTAL_SCORE) of the team
            and also set the individual score (__scores) of the player
        '''

        # Player.addScore(scores)
        Player.TOTAL_SCORE = Player.TOTAL_SCORE + scores - self.__scores
        self.__scores = scores

    def getScores(self):
        ''' return individual score (__scores) of the player '''
        return self.__scores

    def setfourRuns(self,fourRuns):
        ''' take fourrun and add these into the fours (__fourRuns) '''
        self.__fourRuns = fourRuns

    def getfourRuns(self):
        ''' return the fours (__fourRuns) of the player '''
        return self.__fourRuns

    def setSixRuns(self,sixRuns):
        ''' take sixrun and add these into the sixes (__sixRuns) '''
        self.__sixRuns = sixRuns

    def getSixRuns(self):
        ''' return the six (__sixRuns) of the player '''
        return self.__sixRuns

    def setBalls(self,ball):
        ''' take ball and add these into the individual played balls (__balls) '''
        self.__balls = self.__balls + ball


    def setStillBatting(self):
        ''' set the stricker and nonstrcicker player status (They are playing or out) '''
        self.__playerName = self.__playerName + '*'

    def setOut(self):
        ''' set the total number of out player for a team (TOTAL_OUT) 
            and set the status of that player with their name '''
        Player.TOTAL_OUT = Player.TOTAL_OUT + 1
        self.__playerName = self.__playerName[:len(self.__playerName)-1]

    def __str__(self):
        ''' Override the __str__ method with out required displayed data '''
        return self.__playerName + '\t\t' + str(self.__scores) + '\t' + str(self.__fourRuns) + '\t' + str(self.__sixRuns) + '\t' + str(self.__balls)

    @staticmethod
    def total_score():
        ''' static method to return the Total score (TOTAL_SCORE) of the Team '''
        return Player.TOTAL_SCORE

    @staticmethod
    def total_out():
        ''' static method to return the Total out (TOTAL_OUT) of the Team '''
        return Player.TOTAL_OUT


if __name__=='__main__':
    p1 = Player('P1',3,0,0,3,stillBatting=True)
    print('Player Name'+'\t'+'Score\t'+'4s\t'+'6s'+'\t'+'Balls')
    print(p1)
    p2 = Player('P2',4,0,0,3,out=True)
    print(p2)
    p3 = Player('P3',4,0,0,3,stillBatting=True)
    print(p3)
    print('Total: '+ str(Player.total_score())+"/"+str(Player.total_out()))


        
