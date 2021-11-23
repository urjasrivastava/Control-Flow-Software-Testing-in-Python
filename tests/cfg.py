from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file('cfg', r'C:\Users\urja\Desktop\Control-Flow-Software-Testing-in-Python\src\Chess.py')
cfg.build_visual('cfg', 'png')
cfg.build_visual('cfg', 'pdf')