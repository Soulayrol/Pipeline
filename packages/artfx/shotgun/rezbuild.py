import os
import shutil


def build(source_path, build_path, install_path, targets):
    def _build():
        src = os.path.join(source_path, "shotgun_api")
        dest = os.path.join(build_path, "shotgun_api")

        if os.path.exists(dest):
            shutil.rmtree(dest)

        shutil.copytree(src, dest)

    def _install():
        src = os.path.join(build_path, "shotgun_api")
        dest = os.path.join(install_path, "shotgun_api")

        if os.path.exists(dest):
            shutil.rmtree(dest)

        shutil.copytree(src, dest)

    _build()

    if "install" in (targets or []):
        _install()
