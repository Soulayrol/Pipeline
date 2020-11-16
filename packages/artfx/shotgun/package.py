name = "shotgun"

version = "0.0.0"

authors = ['ArtFx TD gang']

description = \
    """
    Shotgun api
    """

requires = [
    "python",
]

tools = [
    "test_shotgun"
]

vcs = "git"

def commands():
    global env
    env.PATH.append("{root}")
    env.PYTHONPATH.append("{root}")
