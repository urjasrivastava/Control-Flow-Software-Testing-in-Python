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
