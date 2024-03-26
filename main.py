from handler import APIHandler
from nuke import NukeFiles

user = APIHandler()
nuke_user = NukeFiles(3, "stats/")
nuke_user.nuke_files()
