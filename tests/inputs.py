"""
        @desc: create user choice input
        @param player: The player which has to move
        @param depth: depth of min max chosen
"""
def valid_moves(player,depth):
    return player.getBestMove(depth)

def invalid_moves(player,depth):
        inputs=["z2z4","z4z7"]
        return inputs