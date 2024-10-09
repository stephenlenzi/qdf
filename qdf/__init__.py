from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("qdf")
except PackageNotFoundError:
    # package is not installed
    pass
