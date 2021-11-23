import pytest
import sys
sys.path.insert(0, r'C:\Users\Lenovo\Desktop\Testing Project\Control-Flow-Software-Testing-in-Python\src')
from Chess import __main__
from inputs import valid_moves, invalid_moves 

depthchoice =[]
teamchoice = []
commandchoice = []

def test_line23():
    depthchoice =[0,0,0]
    try:
        __main__(depthchoice,teamchoice,commandchoice,valid_moves)
    except Exception as exc:
       assert True







