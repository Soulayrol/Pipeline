import os
import shutil


def build(source_path, build_path, install_path, targets):

    def _build():
        for name in ("config", "lib"):
            src = os.path.join(source_path, name)
            dest = os.path.join(build_path, name)

            if os.path.exists(dest):
                shutil.rmtree(dest)

            shutil.copytree(src, dest)


    def _install():
        for name in ("config", "lib"):
            src = os.path.join(build_path, name)
            dest = os.path.join(install_path, name)

            if os.path.exists(dest):
                shutil.rmtree(dest)

            shutil.copytree(src, dest)

    _build()

    if "install" in (targets or []):
        _install()
