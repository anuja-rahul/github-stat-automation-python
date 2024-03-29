from handler import APIHandler
from nuke import NukeFiles

user = APIHandler()
nuke_user = NukeFiles(1, "stats/")
nuke_user.nuke_files()
