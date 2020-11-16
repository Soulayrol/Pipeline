import os
import sys

import maya.standalone
import mayaLib

print("=" * 30)
print("This is mayaLib package test")
print("=" * 30)

print("Initializing maya standalone ...")
maya.standalone.initialize(name="python")

# Create engine
maya_engine = mayaLib.MayaEngine()
print("Engine : " + str(maya_engine))
# Get engine path
print("Current file location : " + str(maya_engine.get_file_path()))
# Save
maya_engine_scene = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop", "test.ma")
maya_engine.save(maya_engine_scene)
print("Current file location after save : " + maya_engine.get_file_path())
# Open as
maya_engine.open_as(maya_engine.get_file_path())
print("Open as ")
print("Current file location after open as : " + maya_engine.get_file_path())
# Open
maya_engine.open(maya_engine_scene)
print("Current file location after open : " + maya_engine.get_file_path())

print("Uninitialized maya standalone ...")
maya.standalone.uninitialize()
sys.exit(0)
