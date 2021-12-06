#game_versus.py

from direct.showbase.ShowBase import ShowBase

from sets import sets
from player import player

class game_versus(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        on_kick = False
        
        self.disableMouse()
        self.setBackgroundColor((0, 0, 0, 1))
        self.backgroundImage = sets("background_versus.png",scale=10)
        self.backgroundImage.getObj().reparentTo(self.render)

        self.player1 = player(tex_wait="sprite_test_wait_blue.png",
                            tex_jump='sprite_test_jump_blue.png',
                            tex_kick_left='sprite_test_kick_left_blue.png',
                            tex_kick_right='sprite_test_kick_right_blue.png',
                            scale=0.3,position=(-2,-1),tskMngr=self.taskMgr)
        self.player1.getObj().reparentTo(self.render)
        self.taskMgr.add(self.player1.move_task, "move_task", extraArgs=[None, 'q', 'd'])
        self.taskMgr.add(self.player1.jump_task, "jump_task", extraArgs=[None, 'z'])
        self.taskMgr.add(self.player1.kick_task, "kick_task", extraArgs=[None, 'a', 'e'])

        self.player2 = player(tex_wait="sprite_test_wait_red.png",
                            tex_jump='sprite_test_jump_red.png',
                            tex_kick_left='sprite_test_kick_left_red.png',
                            tex_kick_right='sprite_test_kick_right_red.png',
                            scale=0.3,position=(2,-1),tskMngr=self.taskMgr)
        self.player2.getObj().reparentTo(self.render)
        self.taskMgr.add(self.player2.move_task, "move_task", extraArgs=[None, 'j', 'l'])
        self.taskMgr.add(self.player2.jump_task, "jump_task", extraArgs=[None, 'i'])
        self.taskMgr.add(self.player2.kick_task, "kick_task", extraArgs=[None, 'u', 'o'])
