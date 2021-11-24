"""
        @desc: create user choice input
        @param player: The player which has to move
        @param depth: depth of min max chosen
"""
counter = 0
def valid_moves(player,depth):
    return player.getBestMove(depth)

def invalid_moves(player,depth):
        global counter
        counter +=1
        if counter<3:
                input="z2z4"
        else :
             input = player.getBestMove(depth)   
        return input