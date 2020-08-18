#--------------- import user-defiend module -------------------------
from cricket_scorecard import scorecard

try:
    numOfPlayers = int(input('No. of players for each team: '))
    numOfOvers = int(input('No. of overs: '))

    ''' calling scorecard function '''
    scorecard(numOfPlayers,numOfOvers)
except Exception as e:
    # print(e)
    print('Invalid ! Please Try again')



