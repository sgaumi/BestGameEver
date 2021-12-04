#set.py

from panda3d.core import Point3, KeyboardButton, TextNode, TransparencyAttrib

class sets():

    def __init__(self, tex_file, background=True, position=(0, 0),
    depth=10,scale=20,transparency=False):
        if background:
            self.set = self.loadObject(tex=tex_file,pos=position,
                depth=depth,scale=scale,transparency=transparency)


    def loadObject(self, tex=None, pos=(0, 0), depth=5, scale=1,
               transparency=False):
        # Every object uses the plane model and is parented to the camera
        # so that it faces the screen.
        obj = loader.loadModel("../data/square")
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
        return self.set