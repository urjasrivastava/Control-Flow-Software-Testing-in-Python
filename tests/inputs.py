"""
        @desc: create user choice input
        @param player: The player which has to move
        @param depth: depth of min max chosen
"""
def valid_moves(player,depth):
    return player.getBestMove(depth)

def invalid_moves(player,depth):
        inputs=["e2e4","e4e7"]
        return inputs