# Keyframe Layer is a Krita plugin to create a new animation layer with a key frame to merge down.
# Copyright (C) 2022  Ricardo Jeremias.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Import Krita
from krita import *
from PyQt5 import QtWidgets, uic


# Set Window Title Name
DOCKER_NAME = "KeyFrame Layer"
layer_name = "temporary"


# Create Docker
class KeyFrame_Layer_Docker(DockWidget):
    """
    KeyFrame Layer
    """

    def __init__(self):
        super(KeyFrame_Layer_Docker, self).__init__()
        self.Interface()
        self.Connections()

    def Interface(self):
        self.setWindowTitle(DOCKER_NAME)
        self.window = QWidget()
        self.layout = uic.loadUi(os.path.dirname(os.path.realpath(__file__)) + '/keyframe_layer.ui', self.window)
        self.setWidget(self.window)
    def Connections(self):
        self.layout.anim_layer_add.clicked.connect(self.Anim_Layer_Add)

    def Anim_Layer_Add(self):
        if ((self.canvas() is not None) and (self.canvas().view() is not None)):
            # Variables
            ki = Krita.instance()
            ad = ki.activeDocument()
            an = ad.activeNode()
            # Nodes
            root = ad.rootNode()
            new_node = ad.createNode(layer_name, "paintLayer")
            root.addChildNode(new_node, None)
            new_node.enableAnimation()
            # Keyframes
            current_time = ad.currentTime()
            ad.setCurrentTime(current_time+1)
            Krita.instance().action('add_blank_frame').trigger()
            ad.setCurrentTime(current_time)
            Krita.instance().action('add_blank_frame').trigger()

    # Change the Canvas
    def canvasChanged(self, canvas):
        pass
