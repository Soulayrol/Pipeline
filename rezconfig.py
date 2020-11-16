import os


###############################################################################
# Paths
###############################################################################

root_packages_path = [
    r"C:\packages",
    r"D:\Pipeline\packages",
]

# The path that Rez will locally install packages to when rez-build is used
local_packages_path = r"C:\packages\build\default"

# The path that Rez will deploy packages to when rez-release is used. For
# production use, you will probably want to change this to a site-wide location.
release_packages_path = r"\\multifct\tools\packages\artfx"


# Use a for loop for child forlder if .rez is present
def child_packages(root):
    if not os.path.isdir(root):
        return
    directory_content = os.listdir(root)
    if ".rez" in directory_content:
        yield root
    else:
        return
    for content in directory_content:
        if content.startswith("_"):
            continue
        package_path = os.path.join(root, content)
        if os.path.isdir(package_path):
            for child_path in child_packages(package_path):
                yield child_path


packages_path = []
for path in root_packages_path:
    packages_path.extend(list(child_packages(path)))

###############################################################################
# Package Resolution
###############################################################################

# Override platform values from Platform.os and arch.
# This is useful as Platform.os might show different
# values depending on the availability of lsb-release on the system.
# The map supports regular expression e.g. to keep versions.

platform_map = {
    "os": {
        r"windows-10(.*)": r"windows-10",                           # windows-10.x.x -> windows-10
        r"Linux-(.*)": r"Linux",                                    # Linux-x.x -> Linux
        r"Ubuntu-14.\d": r"Ubuntu-14",                              # Any Ubuntu-14.x      -> Ubuntu-14
        r'CentOS Linux-(\d+)\.(\d+)(\.(\d+))?': r'CentOS-\1.\2',    # Centos Linux-X.Y.Z -> CentOS-X.Y
    },
    "arch": {
        "x86_64": "64bit",
        "amd64": "64bit",
    }
}
