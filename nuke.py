import os
import datetime


class NukeFiles:
    def __init__(self, days: int = 30, path: str = "stats"):
        self.__days = days
        self.__path = path
        self.__time_now = datetime.datetime.now()

    def nuke_files(self):
        for subdirs, dirs, files in os.walk(self.__path):
            for file in files:
                file_path = os.path.join(subdirs, file)
                if os.path.isfile(file_path):
                    file_origin_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                    if self.__time_now - file_origin_time > datetime.timedelta(days=self.__days):
                        print(file_path)
                        os.remove(file_path)
