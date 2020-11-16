name = "checkLib"

version = "0.0.0"

authors = ["ArtFx TD gang"]

description = \
    """
    Python Scripts
    Scripts for qualityCheck
    """

requires = [
    "python",
    "actionLib",
]

vcs = "git"

def commands():
    global env
    env.PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib")


"""
# TODO


def pre_test_commands():
    env.PATH.append("{root}/tests")
    env.PYTHONPATH.append("{root}/tests")

tests = {
    "unit": "python -m unittest discover -s {root}/tests",
    "lint": {
        "command": "pylint scripts",
        "requires": ["pylint"],
        "run_on": ["default", "pre_release"]
    },
    "maya": {
        "command": "mayapy {root}/tests/maya_test.py",
        "requires": ["mayaLib", "maya"],
        "on_variants": {
            "type": "requires",
            "value": ["maya"]
        },
        "run_on": "explicit"
    },
    "houdini": {
        "command": "python {root}/tests/houdini.py",
        "requires": ["houdiniLib"],
        "on_variants": {
            "type": "requires",
            "value": ["maya"]
        },
        "run_on": "explicit"
    },
    "nuke": {
        "command": "python {root}/tests/nuke.py",
        "requires": ["nukeLib"],
        "on_variants": {
            "type": "requires",
            "value": ["maya"]
        },
        "run_on": "explicit"
    }
}

"""
