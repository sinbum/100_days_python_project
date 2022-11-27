import datetime
import pytz


class TimeConvert:
    def __init__(self, **kwargs):
        self.seconds = None
        self.minutes = None
        self.hour = None
        self.day = None
        self.month = None
        self.year = None
        return

    def set_all_time(self, time):
        # 2022-11-27T08:16:20+00:00
        YYYYMMDD = time.split("T")[0]
        hhmmss = time.split("T")[1].split('+')[0]
        self.year = int(YYYYMMDD.split("-")[0])
        self.month = int(YYYYMMDD.split("-")[1])
        self.day = int(YYYYMMDD.split("-")[2])
        self.hour = int(hhmmss.split(":")[0])
        self.minutes = int(hhmmss.split(":")[1])
        self.seconds = int(hhmmss.split(":")[2])

    def get_datetime_class(self):
        dt = datetime.datetime(
            year=self.year,
            month=self.month,
            day=self.day,
            hour=self.hour,
            minute=self.minutes,
            second=self.seconds,
            tzinfo=(pytz.timezone('UTC'))
        ).astimezone(pytz.timezone('Asia/Seoul'))
        return dt
