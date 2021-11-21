"""
        @desc: create user choice input
        @param player: The player which has to move
        @param depth: depth of min max chosen
"""
def moves(player,depth):
    return player.getBestMove(depth)