name = "mayaLib"

version = "0.0.0"

authors = ["ArtFx TD gang"]

description = \
    """
    Python maya Packages.
    Use to converse with Maya dcc
    """

requires = [
    "python",
    "maya",
    "engineLib"
]

tools = [
    "test_maya"
]

vcs = "git"


def commands():
    global env
    env.PATH.append("{root}/lib")
    env.PYTHONPATH.append("{root}/lib")


tests = {
    "unit": "python -m unittest discover -s {root}/tests",
    "lint": {
        "command": "pylint scripts",
        "requires": ["pylint"],
        "run_on": ["default", "pre_release"]
    },
    "maya": {
        "command": "mayapy {root}/tests/maya_test.py",
        "run_on": "explicit"
    },
}
