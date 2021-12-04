#game_versus.py

from direct.showbase.ShowBase import ShowBase

from sets import sets
from player import player

class game_versus(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()
        self.setBackgroundColor((0, 0, 0, 1))
        self.backgroundImage = sets("background_versus.png",scale=10)
        self.backgroundImage.getObj().reparentTo(self.render)

        self.player1 = player("sprite_test_wait_blue.png",scale=0.3,position=(-2,-1))
        self.player1.getObj().reparentTo(self.render)
        self.taskMgr.add(self.player1.move_task, "move_task", extraArgs=[None, 'q', 'd'])

        self.player2 = player("sprite_test_wait_red.png",scale=0.3,position=(2,-1))
        self.player2.getObj().reparentTo(self.render)
        self.taskMgr.add(self.player2.move_task, "move_task", extraArgs=[None, 'j', 'l'])