import panda3d as pd3d

from direct.gui.OnscreenText import OnscreenText
textObject = OnscreenText(text='bestgame ever', pos=(-0.5, 0.02), scale=0.07)

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3, KeyboardButton


class MyApp(ShowBase):


    def __init__(self):
        ShowBase.__init__(self)
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        
        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.001, 0.0005, 0.0005)
        self.pandaActor.setPos(0, 5, -0.3)
        self.pandaActor.setHpr(90, 0, 0)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.

        self.taskMgr.add(self.move_task, "move_task")
        self.taskMgr.add(self.jump_task, "jump_task")

    def jump_task(self,task) :

        
        z = self.pandaActor.getZ()
        if z <= -0.3 :
            is_down = base.mouseWatcherNode.is_button_down
            space_button = KeyboardButton.space()
            if is_down(space_button):
                self.taskMgr.add(self.up,"up")
                print('lee-sin = noob')
        """x_delta = speed * globalClock.get_dt()
        position = self.pandaActor.getPos()"""
    
        return Task.cont

    def up(self,task) :
        speed_jumpu = 2.5
        z_delta = speed_jumpu * globalClock.get_dt()
        z = self.pandaActor.getZ()
        self.pandaActor.setZ(z + z_delta)

        if z + z_delta > 0.3 :
            self.taskMgr.add(self.down,"down")
            return Task.done
        else :
            return Task.cont

    def down(self,task) :
        speed_jumpd = 1.5
        z_deltad = speed_jumpd * globalClock.get_dt()
        zd = self.pandaActor.getZ()
        self.pandaActor.setZ(zd - z_deltad)

        if zd + z_deltad <= -0.3 :
            self.pandaActor.setZ(-0.3)
            return Task.done
        else :
            return Task.cont
        
    def move_task(self, task):
        speed = 0
        right_speed = 1 # units per second
        left_speed = 1
        right_button = KeyboardButton.ascii_key('d')
        left_button = KeyboardButton.ascii_key('q')
        # Check if the player is holding W or S
        
        is_down = base.mouseWatcherNode.is_button_down

        if is_down(right_button):
            speed += right_speed

        if is_down(left_button):
            speed -= left_speed

        if speed > 0 :
            self.pandaActor.setHpr(90, 0, 0)
        elif speed < 0 :
            self.pandaActor.setHpr(-90, 0, 0)
        # Move the player
        x_delta = speed * globalClock.get_dt()
        position = self.pandaActor.getPos()

        self.pandaActor.setPos(position + Point3(x_delta,0,0))
        return Task.cont


app = MyApp()
app.run()
