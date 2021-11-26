import pytest
import sys
sys.path.insert(0, r'C:\Users\Lenovo\Desktop\Testing Project\Control-Flow-Software-Testing-in-Python\src')
from Chess import __main__ 
from inputs import valid_moves, invalid_moves
import inputs

depthchoice =[]
teamchoice = []
commandchoice = []
draws = ["draw"]*60

#tests the depth choice <1 while loop
def test_line23():
    depthchoice =[0,0,0]
    try:
        __main__(depthchoice,teamchoice,commandchoice,valid_moves)
    except Exception as exc:
       assert True

#tests the invalid team choice loop
def test_line29():
    depthchoice = [1,1,1]
    teamchoice = ["R"]    
    try:
        __main__(depthchoice,teamchoice,commandchoice,valid_moves)
    except Exception as exc:
       assert True

#tests the command choice invalid loop
def test_line57():
    depthchoice = [1,1,1]
    teamchoice = ["B"]  
    commandchoice= ["invalid"]  
    try:
        __main__(depthchoice,teamchoice,commandchoice,valid_moves)
    except Exception as exc:
       assert True

#tests the if condition where the game ends in draw
def test_line61():
    #commandchoice.clear()
    depthchoice =[1]
    teamchoice = ["B"]
    commandchoice = ['draw']
    commandchoice.extend(draws) 
    try:
       __main__(depthchoice,teamchoice,commandchoice,valid_moves)
    except Exception as exc:
       assert False   

    #assert (__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

def test_line64():
    #commandchoice.clear()
    depthchoice =[1]
    teamchoice = ["B"]
    #commandchoice.extend(["move"]*10)
    commandchoice = ['draw']
    #commandchoice.extend(draws)
    try:
        __main__(depthchoice,teamchoice,commandchoice,valid_moves)
    except Exception as exc:
       assert True   

def test_line68():
    depthchoice =[1]
    teamchoice = ["B"]
    commandchoice = ['help']
    commandchoice.extend(draws)
    assert (__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#this one goes inside the while loop
def test_line86():
    depthchoice =[1]
    teamchoice = ["B"]
    commandchoice = ['move']
    commandchoice.extend(draws)
    assert (__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)

#this one does not go in while loop
def test_line85():
    depthchoice =[1]
    teamchoice = ["B"]
    commandchoice = ['move']
    commandchoice.extend(draws)
    assert (__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#this one does not go in while loop
def test_line96():
    depthchoice =[1]
    teamchoice = ["W"]
    commandchoice = ['move']
    commandchoice.extend(draws)
    assert (__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)

#lets see if this goes inside the while loop
def test_line94():
    depthchoice =[1]
    teamchoice = ["W"]
    commandchoice = ['move']
    commandchoice.extend(draws)
    inputs.counter=0
    assert (__main__(depthchoice,teamchoice,commandchoice,invalid_moves)==0)









    






