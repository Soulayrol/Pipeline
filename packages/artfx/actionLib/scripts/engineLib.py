import os

def get():
    """
    Get the correct engine
    """
    request = os.getenv("REZ_USED_REQUEST")
    if "maya" in request:
        from mayaLib import MayaEngine
        return MayaEngine()
    elif "houdini" in request:
        from houdiniLib import HoudiniEngine
        return HoudiniEngine()
    elif "nuke" in request:
        from nukeLib import NukeEngine
        return NukeEngine()
    else:
        from engine import Engine
        print("Careful: no engine found, use engine (only few valid methods)")
        return Engine()
