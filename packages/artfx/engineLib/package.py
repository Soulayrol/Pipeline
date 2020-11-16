name = "filesystem"

version = "0.0.0"

authors = ['ArtFx TD gang', 'michael.haussmann']

description = \
    """
    Python-based fileSystem Packages.
    A simple lib for get data from the file system (windows / linux)
    """

requires = [
    "python",
    "Lucidity",
    "six",
]

vcs = "git"

def commands():
    global env
    env.PYTHONPATH.append("{root}")
    env.PYTHONPATH.append("{root}")
