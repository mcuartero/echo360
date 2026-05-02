import os

def naive_versiontuple(v):
    """
    This only works for version tuple with the same number of parts.
    Expects naive_versiontuple('xx.yy.zz') < naive_versiontuple('aa.bb.cc').
    """
    return tuple(map(int, (v.split("."))))


PERSISTENT_SESSION_FOLDER = os.path.join(os.path.expanduser("~"), "echo360_session", "chrome_data")
