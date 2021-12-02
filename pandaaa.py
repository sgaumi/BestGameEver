import panda3d as pd3d

from direct.gui.OnscreenText import OnscreenText
textObject = OnscreenText(text='bestgame ever', pos=(-0.5, 0.02), scale=0.07)

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

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
        
        # Add the spinCameraTask procedure to the task manager.
        #self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        #self.taskMgr.add(self.spinCameraTask2, "SpinCameraTask2")
        
        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.001, 0.0005, 0.0005)
        self.pandaActor.setPos(0, 5, -0.3)
        self.pandaActor.setHpr(90, 0, 0)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.

        self.accept('d', self.move_right,[1] )
        self.accept("d-up", self.move_right, [0])
        self.accept('q', self.move_left,[1] )
        self.accept("q-up", self.move_left, [0])
        self.accept('space', self.jump )


    def move_right(self, value) :
        self.pandaActor.setHpr(90, 0, 0)
        global posInterval1
        position = self.pandaActor.getPos()
 
        if value ==1 :
            posInterval1 = self.pandaActor.posInterval(100,
                                                       position + Point3(20,0,0),
                                                       startPos=position)
            posInterval1.start()
            self.pandaActor.loop("walk")
        else :
            posInterval1.pause()
            self.pandaActor.stop()

    def move_left(self, value) :
        self.pandaActor.setHpr(-90, 0, 0)
        global posInterval2
        position = self.pandaActor.getPos()
 
        if value ==1 :
            posInterval2 = self.pandaActor.posInterval(100,
                                                       position + Point3(-20,0,0),
                                                       startPos=position)
            posInterval2.start()
            self.pandaActor.loop("walk")
        else :
            posInterval2.pause()
            self.pandaActor.stop()

    def jump(self) :

        position = self.pandaActor.getPos()
        posInterval3 = self.pandaActor.posInterval(0.5,
                                                       position + Point3(0,0,0.4),
                                                       startPos=position)
        posInterval4 = self.pandaActor.posInterval(0.5,
                                                       position,
                                                       startPos=position + Point3(0,0,0.4))
        Sequence(posInterval3,posInterval4).start()
        

app = MyApp()
app.run()
