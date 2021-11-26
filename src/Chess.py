from Board import Board
from Player import Player

board = Board()
def checkIfGameHasEnded():

    if board.isCheckmate("B"):
        print("The game has ended. {} has won.".format("White"))
        return

    if board.isCheckmate("W"):
        print("The game has ended. {} has won.".format("Black"))
        return

    if board.isStalemate("W") or board.isStalemate("B"):
        print("The game has ended in a draw.")
        return

def __main__(depthChoice,teamChoice,commandChoice,moves):
    #What depth would like the AI to reach? Type an integer: 
    depth = depthChoice.pop(0)
    #What depth would like the AI to reach? Type an integer: 
    while depth < 1:
        depth =  depthChoice.pop(0)
           
    #What team would like be on? Type 'W' for white and 'B' for black: 
    team = teamChoice.pop(0)
    #What team would like be on? Type 'W' for white and 'B' for black: 
    while team not in ['W', 'B']:
        team = teamChoice.pop(0)

    if team == "W":
        aiTeam = "B"
    else:
        aiTeam = "W"

    board.fillBoard()

    player1 = Player(team, board, False)
    player2 = Player(aiTeam, board, True)

    if team == "W":
        startingPlayer = player1
        otherPlayer = player2
    else:
        startingPlayer = player2
        otherPlayer = player1

    board.declareAsAI(aiTeam)

    board.printBoard()

    while True:
        #Type a command (type 'help' for a list of possible commands.): 
        command = commandChoice.pop(0)
        #Type a command (type 'help' for a list of possible commands.):
        while command not in ["draw", "help", "move"]:
            command = commandChoice.pop(0)

        if command == "draw":
            if board.canDeclareDraw() == True:
                print("The game has ended in a draw.")
                break
            else:
                print("The game not be declared as a draw currently. Current count without a pawn move or capture: {}. Make a move.".format(
                    board.counter))

        elif command == "help":
            print("The following are the list of commands: ")
            print("help: Provides a list of possible commands.")
            print(
                "draw: Ends the game in a draw if 50 moves have been made without a pawn capture or move.")
            print("move: Allows user to make a move.")

        else:

            checkIfGameHasEnded()

            if startingPlayer.isAI == True:
                print("----- AI MOVE -----")
                startingPlayer.move(startingPlayer.getBestMove(depth))
                board.printBoard()
                checkIfGameHasEnded()
                #Type in a move in the format x1y1x2y2 (ex: e2e4): 
                move = moves(otherPlayer,depth)
                while move not in otherPlayer.getAllPossibleMoves():
                    print("{} is an invalid move. Try again.".format(move)) #Type in a move in the format x1y1x2y2 (ex: e2e4): 
                    move = moves(otherPlayer,depth)

                otherPlayer.move(move)

            else:
                #Type in a move in the format x1y1x2y2 (ex: e2e4): 
                move = moves(startingPlayer,depth)
                while move not in startingPlayer.getAllPossibleMoves():
                    print("{} is an invalid move. Try again.".format(move)) #Type in a move in the format x1y1x2y2 (ex: e2e4): 
                    move = moves(startingPlayer,depth)
                        
                startingPlayer.move(move)
                board.printBoard()

                checkIfGameHasEnded()

                print("----- AI MOVE -----")
                otherPlayer.move(otherPlayer.getBestMove(depth))

            board.printBoard()
    return 0