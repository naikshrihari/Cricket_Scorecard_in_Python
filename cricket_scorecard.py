#-------- import class of Player from user-defiend module ------------
from players import Player

#------ define all the global variables ----------------
strickPlayer = None         # on strick batting player
nonStrickPlayer = None      # on non-strick batting player

playerObjectList = None     # store data of the all playing player in a list
index = 1                   # using to increase the index(of playerObjectList) 
                            # when any player will out
scores = []                 # store the score of both teams
OVERS = 0                   # store the Total Overs played by Team
BALLS = 0                   # store the Total Balls of Current over played by Team 
TOTAL_OVERS = None          # store the Total Over with Balls (0.0 in format)



def display(playerObjectList):
    ''' take the list of Player Objects and display Scorecard 
        In screcard : Player Name, Score, 4s, 6s, balls 
                      Total: 
                      Extras:
                      Overs: 
    '''

    print()
    print('Player Name'+'\t'+'Score\t'+'4s\t'+'6s'+'\t'+'Balls')
    for i in playerObjectList:
        print(i)
    print('Total: '+ str(Player.total_score())+"/"+str(Player.total_out()))
    print('Extras: '+str(Player.EXTRAS))
    print('Overs: '+TOTAL_OVERS)


def teamWinCheck(team1, team2):
    ''' take the total scores for both teams and display the winning team 
        Team 1 will win by Total run and Team 2 will win by Total Wickets
    '''
    if team1 > team2:
        return f'Result: Team 1 won the match by {abs(team1-team2)} runs'
    else:
        return f'Result: Team 2 won the match by {abs((len(playerObjectList)-1)-Player.TOTAL_OUT)} Wickets'



def resetStaticVar():
    ''' reset the static variables of the Player class for both teams '''
    Player.resetVar()



def createPlayersObjectList(numOfPlayers):
    ''' take the number of the players for each team and create 
        a list of objects of the Player class 
        which have name of the Players '''
    nameOfPlayersteam = []  # store the names of the players
    player = 1              # starting from the 1st player
    while(numOfPlayers>=player):
        nameOfPlayersteam.append(input())  # take the name of the player and store into it
        player += 1
    
    # print(','.join(nameOfPlayersteam))

    return [Player(playerName=name) for name in nameOfPlayersteam] # creating object store



def changeBattingPlayerStatus(strickPlayer):
    ''' take player object and set their batting status '''
    strickPlayer.setStillBatting()



def evenRun(ballResult, strickPlayer, nonStrickPlayer, lastBall):
    ''' taking ballResult(run of that ball which is even like (0,2,4,6)), 
        strickPlayer(object), nonStrickPlayer(object), lastBall(boolean last ball or not) 
        and add all the required inforamtion (Total Scores, Individual Score, 
        Balls played by that player, fours/sixes and if last ball then change 
        the stricks of the batsman else not changing their stricks) of that 
        player and team to the Player class and return strickPlayer, nonStrickPlayer
    '''
    strickPlayer.setScores(strickPlayer.getScores()+ ballResult)   # adding scores
    strickPlayer.setBalls(1)                                       # adding ball played

    ''' taking care of fours (4s) '''
    if ballResult==4:
        strickPlayer.setfourRuns(strickPlayer.getfourRuns()+1)     # adding 4s
    # taking care of sixs (6s)
    elif ballResult==6:
        strickPlayer.setSixRuns(strickPlayer.getSixRuns()+1)       # adding 6s

    ''' taking care of last ball '''
    if lastBall:
        strickPlayer, nonStrickPlayer = nonStrickPlayer, strickPlayer  # changing the stricks

    return strickPlayer, nonStrickPlayer



def oddRun(ballResult, strickPlayer, nonStrickPlayer, lastBall):
    ''' taking ballResult(run of that ball which is odd like (1,3)), 
        strickPlayer(object), nonStrickPlayer(object), lastBall(boolean last ball or not) 
        and add all the required inforamtion (Total Scores, Individual Score, 
        Balls played by that player, fours/sixes and if last ball then not change 
        the stricks of the batsman else changing their stricks) of that 
        player and team to the Player class and return strickPlayer, nonStrickPlayer
    '''
    strickPlayer.setScores(strickPlayer.getScores()+ballResult)     # adding scores 
    strickPlayer.setBalls(1)                                        # adding balls played
    # print(strickPlayer)

    ''' taking care of other than last ball '''
    if not lastBall:
        strickPlayer, nonStrickPlayer = nonStrickPlayer, strickPlayer

    # print('after ball',strickPlayer)
    return strickPlayer, nonStrickPlayer



def runBall(ballResult, strickPlayer, nonStrickPlayer, lastBall=False):
    ''' taking ballResult, strickPlayer(object), nonStrickPlayer(object),
        lastBall(boolean last ball or not) and divided into the even runs 
        (0/2/4/6) and odd runs (1/3) and work on and return strick and 
        non-strick player '''

    ''' working on odd runs '''
    if ballResult%2!=0:
        strickPlayer, nonStrickPlayer = oddRun(ballResult, strickPlayer, nonStrickPlayer, lastBall)
    # working on even runs
    else:
        strickPlayer, nonStrickPlayer = evenRun(ballResult, strickPlayer, nonStrickPlayer, lastBall)

    return strickPlayer, nonStrickPlayer



def legalDelivery(ballResult, ballNumber, strickPlayer, nonStrickPlayer):
    ''' taking  ballResult, ballNumber, strickPlayer, nonStrickPlayer and working 
        on runs (1/2/3/4/6) and also taking care for last ball strick change
        and return strick and non strick player '''
    ballResult = int(ballResult)            # converted into integer as runs
    # print(ballResult,'BallResult')
    # print(ballNumber,'ballNumber')

    ''' taking care of invalid runs like 5 and runs are always greater 
        than Zero(0) and less than or equal to 6 '''
    if ballResult!=5 and ballResult<=6 and ballResult>0:  
        ''' working on not a last ball '''  
        if ballNumber<6:
            strickPlayer, nonStrickPlayer = runBall( ballResult, strickPlayer, nonStrickPlayer)
        else:
            ''' working on last ball using lastBall flage '''
            strickPlayer, nonStrickPlayer = runBall( ballResult, strickPlayer, nonStrickPlayer,lastBall=True)
    else:
        print('Invalid run !!!!')

    return strickPlayer, nonStrickPlayer



def illeagalDelivery(ballResult, strickPlayer, nonStrickPlayer):
    ''' taking  ballResult, strickPlayer, nonStrickPlayer and working 
        on Wide Ball (Wb/WB/wb/wB) and Wicket (W/w) and return strick 
        and non strick player '''

    ''' taking care of Wide Ball (WB) '''
    if ballResult.upper()=='WB':
        Player.addScore()           # adding extra score to the Team runs
    
    ''' taking care of Wicket (W/w) '''
    if ballResult.upper()=='W':
        strickPlayer.setBalls(1)    # adding balls to the individual played ball of player
        strickPlayer.setOut()       # setting out status to that player
        global index                # using global variable for next player play
        index += 1                  # increasing by 1 for next player play

        ''' taking next player from player object list and changing their playing status  '''
        if index <= len(playerObjectList)-1:
            strickPlayer = playerObjectList[index]      # taking next player
            changeBattingPlayerStatus(strickPlayer)     # changing status

    return strickPlayer, nonStrickPlayer



def withoutNoBall(ballResult, ballNumber, strickPlayer, nonStrickPlayer):
    ''' taking ballResult, ballNumber, strickPlayer, nonStrickPlayer and 
        working on runs/Wide/Wicket and return strick and non-strick '''

    ''' working on runs 1/2/3/4/6 '''
    if ballResult.isdigit():    
        # print('legalDelivery')
        strickPlayer, nonStrickPlayer = legalDelivery(ballResult, ballNumber, strickPlayer, nonStrickPlayer)
    # working on other than 1/2/3/4/6 except no-balls
    else:
        # print('illegalDelivery')
        strickPlayer, nonStrickPlayer = illeagalDelivery(ballResult, strickPlayer, nonStrickPlayer)

    return strickPlayer, nonStrickPlayer



def ballStatus(strickPlayer, nonStrickPlayer, secondInnings):
    ''' taking strickPlayer, nonStrickPlayer, secondInnings as parameters 
        and accepting the runs/wide/Wicket/No-balls on every ball as ballResult
    '''
    global BALLS                # using BALLS as global variable
    ballNumber = 1              # initialize the ballnumber

    while(ballNumber<=6):       # for every ball
        # print(Player.TOTAL_OUT)

        ''' taking care of all out for the team '''
        if Player.TOTAL_OUT < (len(playerObjectList)-1):
            ''' taking care of secound innings wins '''
            if secondInnings and Player.TOTAL_SCORE>scores[0]:
                break
            
            ''' ballResult can be (1/2/3/4/6/W/w/Wb/WB/wb/NB1/NB2/NB3/Nb4/NB6/NBWD) '''
            ballResult = input()       #  accepting the runs/wide/Wicket/No-balls
                                       #  on every ball as ballResult

            ''' taking care of No-ball input given for this (NB1/NB2/NB3/Nb4/NB6/NBWD) '''
            if 'NB' in ballResult.upper():
                if ballResult.upper()[:2] == 'NB':    
                    ballNumber -= 1                     # ball not considered as legal 
                    Player.addScore()                   # adding 1 extra run in Team score
                    ballResult = ballResult.upper()[2:] # finding runs on No-ball

                    ''' working with runs on no-ball and store   the  strick and nonstrick player with strick change if needed '''
                    strickPlayer, nonStrickPlayer = withoutNoBall(ballResult, ballNumber, strickPlayer, nonStrickPlayer)   
            # taking care of other than No-ball      
            else:
                ''' working without No-ball and store the strick and nonstrick player with strick change if needed '''
                strickPlayer, nonStrickPlayer = withoutNoBall(ballResult, ballNumber, strickPlayer, nonStrickPlayer)

            ''' if legal delivery then increase the balls for that over (other than Wide ball only because No-ball already taken care ) '''
            if ballResult.upper()!='WB':
                ballNumber += 1
        # when 2nd Team successfully chased to 1st Team    
        else:
            break
    
    BALLS = ballNumber      # change the global variable BALLS with current played balls
   
    

def overStatus(numOfPlayers, numOfOvers, strickPlayer, nonStrickPlayer, secondInnings):
    ''' taking numOfPlayers, numOfOvers, strickPlayer(object of player),
        nonStrickPlayer(object of player), secondInnings(boolean) 
        and returning the total score of the team
    '''
    overNum = 1                                 
    global OVERS, BALLS, TOTAL_OVERS        # using global variable for overs

    while(numOfOvers >= overNum):           # each over
        print('Over '+str(overNum)+':')
        ballStatus(strickPlayer, nonStrickPlayer, secondInnings)   # working on every balls

        ''' for managing the Overs with ball for displaying Over played by team '''
        if BALLS >= 6:
            OVERS = overNum
            BALLS = 0
        else:
            BALLS -= 1
        TOTAL_OVERS = str(OVERS)+'.'+str(BALLS)     
        # print(TOTAL_OVERS)

        overNum += 1        # adding over by one
        
        display(playerObjectList)       # display the scoreboard after over completed
    
    return Player.TOTAL_SCORE
 
        
    
def scorecard(numOfPlayers,numOfOvers):
    ''' taking numOfPlayers,numOfOvers and display the scorecard 
        after every overs, every innings and at the end, 
        its also show the Winning Team with run margin/wickets 
    '''
    global scores                   # using scores as global variable for both teams
    for teamNum in range(1,3):      # working for each team
        resetStaticVar()            # reset the static variable for every team
        print(f'\nBatting Order for team {teamNum}:')

        global playerObjectList, OVERS, BALLS           # using global variable for each team
        OVERS = BALLS = 0                               # setting the variable as 0  

        playerObjectList = createPlayersObjectList(numOfPlayers)  # creating list of objects
        # display(playerObjectList)

        global strickPlayer,nonStrickPlayer   # using global variable for batting player        
        strickPlayer = playerObjectList[0]    # batsman on strick 
        nonStrickPlayer = playerObjectList[1] # batsman on nonstrick

        changeBattingPlayerStatus(strickPlayer)         # status change on strick
        changeBattingPlayerStatus(nonStrickPlayer)      # status change on nonstrick

        # print(strickPlayer, nonStrickPlayer)
        # taking care of second Inning
        secondInnings = False
        if teamNum == 2:
            secondInnings = True

        # finding the score of team and store into the score list
        scores.append(overStatus(numOfPlayers, numOfOvers, strickPlayer, nonStrickPlayer, secondInnings))

        # display the scorecard team-wise
        print('\n\n')
        print(f'Scorecard for Team {teamNum}:')
        display(playerObjectList)
        
        # print(scores)

    # print(scores)
    

    print(teamWinCheck(*scores))        # seding the scores of both team and find the winner

    






