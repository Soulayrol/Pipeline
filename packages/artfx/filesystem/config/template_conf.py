"""

CONF FILE FOR FILESYSTEM LOCATION

"""
from collections import OrderedDict

###########################################################################################
# SOFT CONFIG
###########################################################################################

"""
SID TEMPLATES AS MEMO
sid_templates = {
    "asset": "{project}/a/{cat}/{name}/{task}/{subtask}/v{version}/{state}/{ext}",
    "shot":  "{project}/s/s{seq}/p{shot}/{task}/{subtask}/v{version}/{state}/{ext}",
    "project": "{project}",
}
"""

###########################################################################################
# PATHS The order is important, first match is returned.
# TODO frame caches, versioned caches, images with passes, etc.
###########################################################################################
path_templates = OrderedDict([
    #  FIXME : {frames} {namespace} not handled yet
    ("project_root", r"I:/SynologyDrive/{project}"),

    ("asset_frame_file", r"{@project_root}/03_WORK_PIPE/{entity:01_ASSET_3D}/{cat}/{name}/{dimension}/{type}/{task}/{subtask}/{state}_v{version}/{name}.{frame}.{ext}"),
    ("asset_file", r"{@project_root}/03_WORK_PIPE/{entity:01_ASSET_3D}/{cat}/{name}/{dimension}/{type}/{task}/{subtask}/{state}_v{version}/{name}.{ext}"),
    ("asset_version", r"{@project_root}/03_WORK_PIPE/{entity:01_ASSET_3D}/{cat}/{name}/{dimension}/{type}/{task}/{subtask}/{state}_v{version}"),
    ("asset_state", r"{@project_root}/03_WORK_PIPE/{entity:01_ASSET_3D}/{cat}/{name}/{dimension}/{type}/{task}/{subtask}/{state}_v{version}"),
    ("asset_subtask", r"{@project_root}/03_WORK_PIPE/{entity:01_ASSET_3D}/{cat}/{name}/{dimension}/{type}/{task}/{subtask}"),
    ("asset_task", r"{@project_root}/03_WORK_PIPE/{entity:01_ASSET_3D}/{cat}/{name}/{dimension}/{type}/{task}"),
    ("asset_type", r"{@project_root}/03_WORK_PIPE/{entity:01_ASSET_3D}/{cat}/{name}/{dimension}/{type}"),
    ("asset_name", r"{@project_root}/03_WORK_PIPE/{entity:01_ASSET_3D}/{cat}/{name}"),
    ("asset_cat", r"{@project_root}/03_WORK_PIPE/{entity:01_ASSET_3D}/{cat}"),

    ("shot_frame_file", r"{@project_root}/03_WORK_PIPE/{entity:02_SHOT}/{dimension}/{type}/s{seq}/p{shot}/{task}/{subtask}/{state}_v{version}/s{seq}_p{shot}.{frame}.{ext}"),
    ("shot_file", r"{@project_root}/03_WORK_PIPE/{entity:02_SHOT}/{dimension}/{type}/s{seq}/p{shot}/{task}/{subtask}/{state}_v{version}/s{seq}_p{shot}.{ext}"),
    ("shot_version", r"{@project_root}/03_WORK_PIPE/{entity:02_SHOT}/{dimension}/{type}/s{seq}/p{shot}/{task}/{subtask}/{state}_v{version}"),
    ("shot_state", r"{@project_root}/03_WORK_PIPE/{entity:02_SHOT}/{dimension}/{type}/s{seq}/p{shot}/{task}/{subtask}/{state}_v{version}"),
    ("shot_subtask", r"{@project_root}/03_WORK_PIPE/{entity:02_SHOT}/{dimension}/{type}/s{seq}/p{shot}/{task}/{subtask}"),
    ("shot_task", r"{@project_root}/03_WORK_PIPE/{entity:02_SHOT}/{dimension}/{type}/s{seq}/p{shot}/{task}"),
    ("shot_shot", r"{@project_root}/03_WORK_PIPE/{entity:02_SHOT}/{dimension}/{type}/s{seq}/p{shot}"),
    ("shot_seq", r"{@project_root}/03_WORK_PIPE/{entity:02_SHOT}/{dimension}/{type}/s{seq}"),
    ("shot_type", r"{@project_root}/03_WORK_PIPE/{entity:02_SHOT}/{dimension}/{type}"),
    
    ("entity", r"{@project_root}/03_WORK_PIPE/{entity}"),
    ("entity", r"{@project_root}/03_WORK_PIPE/{entity}/{dimension}"),

    ("project", r"{@project_root}"),

])

path_templates_reference = "project_root"

path_defaults = {
    "dimension": "*",
    "frame": "#",
    "type": "scenes",
}

""" If entity check dimention, if not exist give value * """
force_path = {
    "entity": ("dimension", "*"),
    "version": ("state", "*"),
    "state": ("version", "*")
}

path_mapping = {  # TODO put into project_conf

    "project": {            # 3 words : initials, otherwise 6 first letters, lowercased
        "BACKSTAGE": "back",
        "BARNEY": "barney",
        "COCORICA": "coco",
        "DIVE": "dive",
        "DREAMBLOWER": "dream",
        "FROM_ABOVE": "above",
        "GOOD_MORNING_KITTY": "kitty",
        "GREEN": "green",
        "HAKAM": "hakam",
        "HOSTILE": "hostile",
        "PIR_HEARTH": "hearth",
        "RELATIVITY": "relativ",
        "A_PIPE": "pipe",
        "DEMO": "demo",
    },
    "entity": {
        "01_ASSET_3D": "a",
        "02_SHOT": "s",
    },
    "state": {
        "work": "w",
        "publish": "p",
    },
    "type": {
        "scenes": "scene",
        "images": "image",
        "caches": "cache",
        "texture": "textures"
    }
}

def get_datatype(data):
    """
    rules defining the sidtype, based on the data dict of the sid.
    The keys are always given.
    The values can be empty.

    :param data:
    :return:
    """
    subtype = "project"

    if "entity" in data.keys():
        subtype = "entity"

    if data.get("type"):
        subtype = "shot_type"

    if "cat" in data.keys():
        subtype = "asset"

        if data.get("cat"):
            subtype = "asset_cat"

        if data.get("name"):
            subtype = "asset_name"

        if data.get("type"):
            subtype = "asset_type"

        if data.get("task"):
            subtype = "asset_task"

        if data.get("subtask"):
            subtype = "asset_subtask"

        if data.get("version"):
            subtype = "asset_version"

        if data.get("state"):
            subtype = "asset_state"

        if data.get("ext"):
            subtype = "asset_file"

    elif "seq" in data.keys():
        subtype = "shot"

        if data.get("seq"):
            subtype = "shot_seq"

        if data.get("shot"):
            subtype = "shot_shot"

        if data.get("task"):
            subtype = "shot_task"

        if data.get("subtask"):
            subtype = "shot_subtask"

        if data.get("version"):
            subtype = "shot_version"

        if data.get("state"):
            subtype = "shot_state"

        if data.get("ext"):
            subtype = "shot_file"

    return subtype
