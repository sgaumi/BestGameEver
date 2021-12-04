#player.py

from panda3d.core import Point3, KeyboardButton, TextNode, TransparencyAttrib
from direct.task import Task

class player():

    def __init__(self, position=(0, 0),
    depth=8,scale=0.2,transparency=True,tskMngr=None,
    tex_wait='sprite_test_wait.png',
    tex_jump='sprite_test_jump.png'):

        self.player = self.loadObject(tex=tex_wait,pos=position,
            depth=depth,scale=scale,transparency=transparency)
        self.taskMgr = tskMngr #on donne acces au task manager de game_versus
        self.tex_jump = tex_jump
        self.tex_wait = tex_wait



    def loadObject(self, tex=None, pos=(0, 0), depth=5, scale=1,
               transparency=False):
        # Every object uses the plane model and is parented to the camera
        # so that it faces the screen.
        obj = loader.loadModel("../data/rectangle")
        #obj.reparentTo(camera)

        # Set the initial position and scale.
        obj.setPos(pos[0], depth, pos[1])
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
            tex = loader.loadTexture("../data/" + tex)
            obj.setTexture(tex, 1)

        return obj

    def getObj(self):
        return self.player

    def move_task(self, task, left_key, right_key):
        speed = 0
        right_speed = 1 # units per second
        left_speed = 1
        right_button = KeyboardButton.ascii_key(right_key)
        left_button = KeyboardButton.ascii_key(left_key)
        # Check if the player is holding W or S
        
        is_down = base.mouseWatcherNode.is_button_down

        if is_down(right_button):
            speed += right_speed

        if is_down(left_button):
            speed -= left_speed

        if speed > 0 :
            self.player.setHpr(0, 0, 0)
        elif speed < 0 :
            self.player.setHpr(0, 0, 0)
        # Move the player
        x_delta = speed * globalClock.get_dt()
        position = self.player.getPos()

        self.player.setPos(position + Point3(x_delta,0,0))
        return Task.cont

    ###jump
    def jump_task(self,task) :
        on_kick=False #enlever plus tard
        
        z = self.player.getZ()
        is_down = base.mouseWatcherNode.is_button_down
        space_button = KeyboardButton.space()
        if is_down(space_button):
            texture = loader.loadTexture("../data/" + self.tex_jump)
            if on_kick != True :
                self.player.setTexture(texture, 1)
            self.taskMgr.add(self.up,"up")
            return Task.done
    
        return Task.cont

    def up(self,task) :
        speed_jumpu = 2.5
        z_delta = speed_jumpu * globalClock.get_dt()
        z = self.player.getZ()
        self.player.setZ(z + z_delta)

        if z + z_delta > 0 :
            self.taskMgr.add(self.down,"down")
            return Task.done
        else :
            return Task.cont

    def down(self,task) :
        
        on_kick=False
        
        speed_jumpd = 2.5
        z_deltad = speed_jumpd * globalClock.get_dt()
        zd = self.player.getZ()
        self.player.setZ(zd - z_deltad)

        if zd + z_deltad <= -1 :
            self.player.setZ(-1)
            texture = loader.loadTexture("../data/" + self.tex_wait)
            if on_kick != True :
                self.player.setTexture(texture, 1)
            self.taskMgr.add(self.jump_task,"jump_task")
            return Task.done
        else :
            return Task.cont
    ###jump-end