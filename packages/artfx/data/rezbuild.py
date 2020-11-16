import os
import shutil


def build(source_path, build_path, install_path, targets):
    def __build__():
        src = os.path.join(source_path, "lib")
        dest = os.path.join(build_path, "lib")

        if os.path.exists(dest):
            shutil.rmtree(dest)

        shutil.copytree(src, dest)

    def __install__():
        src = os.path.join(build_path, "lib")
        dest = os.path.join(install_path, "lib")

        if os.path.exists(dest):
            shutil.rmtree(dest)

        shutil.copytree(src, dest)

    _build()

    if "install" in (targets or []):
        _install()
