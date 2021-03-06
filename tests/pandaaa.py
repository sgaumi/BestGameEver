import panda3d as pd3d
import numpy as np

from direct.gui.OnscreenText import OnscreenText
textObject = OnscreenText(text='bestgame ever', pos=(-0.8, 0.6), scale=0.07)

from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3, KeyboardButton
from panda3d.core import TextNode, TransparencyAttrib

def loadObject(tex=None, pos=Point3(0, 0), depth=5, scale=1,
               transparency=True):
    # Every object uses the plane model and is parented to the camera
    # so that it faces the screen.
    obj = loader.loadModel("modelo/plane")
    #obj.reparentTo(camera)

    # Set the initial position and scale.
    obj.setPos(0, depth, -0.3)
    obj.setScale(scale)

    # This tells Panda not to worry about the order that things are drawn in
    # (ie. disable Z-testing).  This prevents an effect known as Z-fighting.
    """obj.setBin("unsorted", 0)
    obj.setDepthTest(False)
    """
    if transparency:
        # Enable transparency blending.
        obj.setTransparency(TransparencyAttrib.MAlpha)

    if tex:
        # Load and set the requested texture.
        tex = loader.loadTexture("modelo/" + tex)
        obj.setTexture(tex, 1)

    return obj


class MyApp(ShowBase):


    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()
        
        self.setBackgroundColor((0, 0, 0, 1))
        self.bg = loadObject("Capture.PNG", scale=20, depth=10,
                             transparency=False)
    
        self.bg.reparentTo(self.render)

        # Load and transform the panda actor.
        self.pandaActor = loadObject("sprite_test_wait.png", scale=0.3, depth=5,
                             transparency=True)
        #self.pandaActor.setScale(0.001, 0.0005, 0.0005)
        self.pandaActor.setPos(0, 5, -0.3)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        
        self.pandababy = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandababy.setScale(0.0004, 0.0002, 0.0002)
        self.pandababy.setPos(1.5, 5, -0.3)
        self.pandababy.setHpr(-90, 0, 0)
        self.pandababy.reparentTo(self.render)
        global score
        global Babyinterval
        global on_kick
        global texture
        on_kick = False

        texture = loader.loadTexture("modelo/" + 'sprite_test_wait.png')
        score = 0
        Babyinterval = self.pandababy.posInterval(2,
                                                   Point3(-2.5, 5, -0.3),
                                                   startPos=Point3(2.5, 5, -0.3))
        Babyinterval.loop()

        self.taskMgr.add(self.move_task, "move_task")
        self.taskMgr.add(self.jump_task, "jump_task")
        self.taskMgr.add(self.collision_task, "collision_task")
        self.taskMgr.add(self.kick_task, "kick_task")

        self.taskMgr.doMethodLater(2, self.score_inc, 'score_inc')


    def kick_task(self,task) :

        global on_kick
        
        is_down = base.mouseWatcherNode.is_button_down
        k_button = KeyboardButton.ascii_key('k')
        j_button = KeyboardButton.ascii_key('j')
        if is_down(k_button):
            on_kick = True
            tex = loader.loadTexture("modelo/" + 'sprite_test_kick_right.png')
            self.pandaActor.setTexture(tex, 1)
            self.taskMgr.doMethodLater(0.3, self.end_kick, 'end_kick')
            return Task.done
        
        elif is_down(j_button):
            on_kick = True
            tex = loader.loadTexture("modelo/" + 'sprite_test_kick_left.png')
            self.pandaActor.setTexture(tex, 1)
            self.taskMgr.doMethodLater(0.3, self.end_kick, 'end_kick')
            return Task.done
        
        return Task.cont

    def end_kick(self,task) :
        global texture
        global on_kick
        self.pandaActor.setTexture(texture, 1)
        self.taskMgr.add(self.kick_task, "kick_task")
        on_kick = False
        return Task.done
    
    def score_inc(self,task) :
        global textObject
        global score
        textObject.destroy()
        textObject = OnscreenText(text='Your score is : ' + str(score), pos=(-0.8, 0.6), scale=0.07)
        score += 1
        return Task.again
    

    def collision_task(self,task) :
        global Babyinterval
        global textObject
        pos1 = self.pandaActor.getPos()
        pos2 = self.pandababy.getPos()
        
        dist = np.linalg.norm(pos1-pos2)

        if dist < 0.15 :
            Babyinterval.finish()
            self.taskMgr.remove('score_inc')
            textObject.destroy()
            textObject = OnscreenText(text='GAME OVER \n FINAL SCORE : ' + str(score), pos=(-0.8, 0.6), scale=0.07)
            return Task.done

        return Task.cont
        
        

    def jump_task(self,task) :

        global texture
        global on_kick
        
        z = self.pandaActor.getZ()
        is_down = base.mouseWatcherNode.is_button_down
        space_button = KeyboardButton.space()
        if is_down(space_button):
            texture = loader.loadTexture("modelo/" + 'sprite_test_jump.png')
            if on_kick != True :
                self.pandaActor.setTexture(texture, 1)
            self.taskMgr.add(self.up,"up")
            print('lee-sin = noob')
            return Task.done
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
        
        global texture
        global on_kick
        
        speed_jumpd = 1.5
        z_deltad = speed_jumpd * globalClock.get_dt()
        zd = self.pandaActor.getZ()
        self.pandaActor.setZ(zd - z_deltad)

        if zd + z_deltad <= -0.3 :
            self.pandaActor.setZ(-0.3)
            texture = loader.loadTexture("modelo/" + 'sprite_test_wait.png')
            if on_kick != True :
                self.pandaActor.setTexture(texture, 1)
            self.taskMgr.add(self.jump_task,"jump_task")
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
            self.pandaActor.setHpr(0, 0, 0)
        elif speed < 0 :
            self.pandaActor.setHpr(0, 0, 0)
        # Move the player
        x_delta = speed * globalClock.get_dt()
        position = self.pandaActor.getPos()

        self.pandaActor.setPos(position + Point3(x_delta,0,0))
        return Task.cont


app = MyApp()
app.run()
