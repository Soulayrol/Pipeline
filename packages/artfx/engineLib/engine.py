import os
import platform
import subprocess
import webbrowser


class Engine(object):

    @staticmethod
    def conform(file_path):
        """
        Replace the os path with pysep change
        """
        file_path = file_path.replace(os.sep, '/')
        return file_path

    def explore(self, path):
        """
        Explore the path in the filesystem.
        :param path: Path to explore.
        """
        if not os.path.exists(path):
            print("Path does not exist: {}".format(path))
            return

        path = os.path.normcase(path)
        if platform.system() == "Windows":
            subprocess.Popen(["explorer", "/open,", path])
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    def open(self, path):
        """
        Open file
        :param str path: The path to the file to open
        """
        webbrowser.open(path)

    def open_as(self, file_path):
        """
        Open file and rename it with a time value
        for keep the source file
        """
        pass

    def save(self, path):
        """
        Save the given scene
        :param str path: Path to the scene file
        """
        pass

    def create_reference(self, path, namespace):
        """
        Create a reference to the scene (path).
        :param str path: Path of the file to reference
        :param str namespace: namespace name of the reference
        """
        pass

    def get_file_path(self):
        """
        Get the current file path (from the current open file)
        :return: The file path of the current scene
        :rtype: str
        """
        pass

    def set_workspace(self, path):
        """
        Set workspace path with the given path.
        :param str path: Workspace path
        """
        pass

    def publish(self):
        """
        Publish the current scene
        """
        pass

    def pre_publish(self):
        """
        Prepare the publish
        """
        pass

    def __str__(self):
        """
        Return the soft name
        """
        return "engine"
