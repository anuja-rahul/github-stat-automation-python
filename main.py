from handler import APIHandler
from nuke import NukeFiles

user = APIHandler()
nuke_user = NukeFiles(7, "stats/")
nuke_user.nuke_files()
