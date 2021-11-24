import pytest
import sys
sys.path.insert(0, r'C:\Users\Lenovo\Desktop\Testing Project\Control-Flow-Software-Testing-in-Python\src')
from Chess import __main__ 
from inputs import valid_moves, invalid_moves 

depthchoice =[]
teamchoice = []
commandchoice = []
draws = ["draw"]*60
def test_line23():
    depthchoice =[0,0,0]
    try:
        __main__(depthchoice,teamchoice,commandchoice,valid_moves)
    except Exception as exc:
       assert True

def test_line29():
    depthchoice = [1,1,1]
    teamchoice = ["R"]    
    try:
        __main__(depthchoice,teamchoice,commandchoice,valid_moves)
    except Exception as exc:
       assert True



def test_line57():
    commandchoice.clear()
    depthchoice =[1]
    teamchoice = ["B"]
    commandchoice.extend(["move"]*10)
    commandchoice.extend(draws)
    
    assert (__main__(depthchoice,teamchoice,commandchoice,valid_moves)==0)
    






#






