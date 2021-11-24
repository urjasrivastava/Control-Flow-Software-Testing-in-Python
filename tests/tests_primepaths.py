import pytest
import sys
sys.path.insert(0, r'C:\Users\urja\Desktop\Control-Flow-Software-Testing-in-Python\src')
from Chess import __main__
from inputs import valid_moves, invalid_moves 

depthchoice =[]
teamchoice = []
commandchoice = []
draws =["draw"]*50

# path -> 0 1 2 1 2 1 3 4 5 4 5 4 6 7 9 10 12 13 14 15 16 15 16 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test1():
    depthchoice.extend([0,0,1])
    teamchoice.extend(['C','C','W'])
    commandchoice.extend(['invalid','invalid','help'])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test2():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(['help'])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 2 1 2 1 3 4 5 4 5 4 6 8 9 11 12 13 14 15 16 15 16 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test3():
    depthchoice.extend([0,0,1])
    teamchoice.extend(['C','C','B'])
    commandchoice.extend(['invalid','invalid','help'])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test4():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(['help'])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 2 1 2 1 3 4 5 4 5 4 6 7 9 10 12 13 14 15 17 19 23 13 14 15 17 19 21 26
def test5():
    depthchoice.extend([0,0,1])
    teamchoice.extend(['C','C','W'])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 19 23 13 14 15 17 19 21 26
def test6():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 2 1 2 1 3 4 5 4 5 4 6 8 9 11 12 13 14 15 17 19 23 13 14 15 17 19 21 26
def test7():
    depthchoice.extend([0,0,1])
    teamchoice.extend(['C','C','B'])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 19 23 13 14 15 17 19 21 26
def test8():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 18 20 25 28 31 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test9():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 18 20 24 27 30 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test10():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 18 20 24 27 29 27 29 27 30 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test11():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)

#path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 18 20 25 28 32 28 32 28 31 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test12():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)

#path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 18 22 13 14 15 17 18 20 25 28 31 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test13():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["help","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 18 22 13 14 15 17 18 20 24 27 30 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test14():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["help","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 19 23 13 14 15 17 18 20 25 28 31 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test15():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["draw","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 19 23 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test16():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["draw","help"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 19 23 13 14 15 17 18 20 24 27 30 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test17():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["draw","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

# path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 19 23 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test18():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["draw","help"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 18 22 13 14 15 17 18 20 25 28 31 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test19():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["help","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)

#path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 18 22 13 14 15 17 18 20 24 27 29 27 29 27 30 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test20():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["help","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)

# path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 19 23 13 14 15 17 18 20 25 28 32 28 32 28 31 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test21():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["draw","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)

# path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 19 23 13 14 15 17 18 20 24 27 29 27 29 27 30 33 13 14 15 17 19 23 13 14 15 17 19 21 26
def test22():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["draw","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)

#path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 18 20 25 28 31 33 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test23():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["move","help"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)

#path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 18 20 24 27 29 27 29 27 30 33 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test24():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["move","help"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)

#path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 18 20 25 28 31 33 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test25():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["help","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 18 20 24 27 30 33 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test26():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["help","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#path -> 0 1 3 4 6 8 9 11 12 13 14 15 17 19 23 13 14 15 17 18 20 24 27 30 33 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test27():
    depthchoice.extend([1])
    teamchoice.extend(['B'])
    commandchoice.extend(["draw","help","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#path -> 0 1 3 4 6 7 9 10 12 13 14 15 17 19 23 13 14 15 17 18 20 25 28 31 33 13 14 15 17 18 22 13 14 15 17 19 23 13 14 15 17 19 21 26
def test28():
    depthchoice.extend([1])
    teamchoice.extend(['W'])
    commandchoice.extend(["draw","help","move"])
    commandchoice.extend(draws)
    assert(__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)


