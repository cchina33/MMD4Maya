import os
import sys

# MMD4Maya package bootstrap for Maya 2025+.
_plugin_file = globals().get('__file__')
if _plugin_file:
    _plugin_dir = os.path.dirname(os.path.realpath(_plugin_file))
else:
    _maya_location = os.environ.get('MAYA_LOCATION')
    _plugin_dir = os.path.join(_maya_location, 'bin', 'plug-ins') if _maya_location else r'C:\Program Files\Autodesk\Maya2025\bin\plug-ins'
_package_dir = os.path.join(_plugin_dir, 'MMD4Maya')
if os.path.isdir(_package_dir):
    __path__ = [_package_dir]
    if _plugin_dir not in sys.path:
        sys.path.insert(0, _plugin_dir)
elif os.path.isdir(os.path.join(_plugin_dir, 'Scripts')):
    __path__ = [_plugin_dir]
    _parent_dir = os.path.dirname(_plugin_dir)
    if _parent_dir not in sys.path:
        sys.path.insert(0, _parent_dir)
import maya.cmds as cmds
import maya.mel as mel
from MMD4Maya.Scripts.UI.MainWindow import *

def ShowMainWindow(*args):
    MainWindow()

def ShowHelp(*args):
    cmds.confirmDialog(title = "Help", message = "\
Steps to import:\n\
1. Select a pmx/pmd file.\n\
2. Select one or multiple vmd files.\n\
3. Check the terms of use then click Process.\n\
\n\
Attention:\n\
1. The file name of fbx file and texture files should not be japanese or chinese.\n\
2. You can only import one model at a time, please save your model as the standard fbx file, then create a new scene to import another one.\n\
\n\
Enjoy! >_< \n\
\n\
Author: Takamachi Marisa\n\
Contact: http://weibo.com/u/2832212042",\
    icon = "information")

def CustomMayaMenu():
    gMainWindow = mel.eval('$temp1=$gMainWindow')
    menus = cmds.window(gMainWindow, q = True, menuArray = True)
    found = False
    
    for menu in menus:
        label = cmds.menu(menu, q = True, label = True)
        if label == "MMD4Maya":
            found = True
    
    if found == False:
        customMenu = cmds.menu(parent=gMainWindow, label = 'MMD4Maya')
        cmds.menuItem(parent = customMenu, label = "Open MMD4Maya", c = ShowMainWindow)
        cmds.menuItem(parent = customMenu, label = "Help", c = ShowHelp)

# Initialize the plug-in
def initializePlugin(plugin):
    CustomMayaMenu()

# Uninitialize the plug-in
def uninitializePlugin(plugin):
    pass