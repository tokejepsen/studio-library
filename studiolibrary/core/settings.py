import os
from . import metafile
__all__ = ['Settings']

class Settings(metafile.MetaFile):
    _instances = {}
    DEFAULT_PATH = os.getenv('APPDATA') or os.getenv('HOME')

    @classmethod
    def instance(cls, *args):
        """
        Return the settings instance for the given scope.

        :type args: list[str]
        :rtype: Settings
        """
        key = '/'.join(args)
        if key not in cls._instances:
            cls._instances[key] = cls(*args)
        return cls._instances[key]

    def __init__(self, *args):
        """
        :type args: list[str]
        """
        self._path = None
        self._args = args
        metafile.MetaFile.__init__(self, '')
        return

    def path(self):
        """
        Return the path.

        :rtype: str
        """
        if not self._path:
            scope = os.path.join(*self._args)
            self._path = os.path.join(Settings.DEFAULT_PATH, scope + '.json')
        return self._path
