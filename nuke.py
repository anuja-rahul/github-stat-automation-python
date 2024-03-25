import os
import datetime


class NukeFiles:
    def __init__(self, days: int = 30, path: str = "logs/"):
        self.__days = days
        self.__path = path
        self.__time_now = datetime.datetime.today()

    def nuke_files(self):
        for subdirs, dirs, files in os.walk(self.__path):
            for file in files:
                file_path = os.path.join(subdirs, file)

                if os.path.isfile(file_path):
                    file_day = int(file.split("-")[0])
                    today = str(self.__time_now.day)
                    day_dif = abs(int(today) - file_day)
                    # print(day_dif)
                    file_origin_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

                    if self.__time_now - file_origin_time > datetime.timedelta(days=self.__days):
                        os.remove(file_path)

                    if day_dif >= self.__days:
                        print(file_path)
                        os.remove(file_path)
