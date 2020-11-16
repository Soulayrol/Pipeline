import engineLib
import data

engine = engineLib.get()

def open(path):
    """
    Open file
    :param str path: The path to the file to open
    """
    engine.open(path)

def save(path):
    """
    Save the given scene
    :param str path: Path to the scene file
    """
    engine.save(path)
