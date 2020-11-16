name = "data"

version = "0.0.0"

authors = ['ArtFx TD gang']

description = \
    """
    Data is a interface for data source (filesystem, bdd, shotgun ...)
    """

requires = [
    "python",
    "filesystem",
    "shotgun",
]

tools = [
    "test_data"
]

vcs = "git"

def commands():
    global env
    env.PATH.append("{root}")
    env.PATH.append("{root}/lib")
