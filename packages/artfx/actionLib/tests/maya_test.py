import os
import sys

import maya.standalone

print("=" * 30)
print("TEST SCRIPT MAYA")
print("=" * 30)

print("Initializing maya standalone ...")
maya.standalone.initialize(name="python")

import scene

print("Current file path: {}".format(scene.get_file_path()))
maya_engine_scene = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop", "test.ma")
print("Save at: {}".format(maya_engine_scene))
scene.save(maya_engine_scene)
print("Open {}".format(maya_engine_scene))
scene.open(maya_engine_scene)

print("Uninitialized maya standalone ...")
maya.standalone.uninitialize()
sys.exit(0)
