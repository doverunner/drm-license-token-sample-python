import re

class PlaybackPolicyRequest:
    def __init__(self, limit=None, persistent=None, duration=None, expire_date=None):
        if limit is None:
            self.__limit = False
        else : 
            self.__limit = limit

        if persistent is None:
            self.__persistent = False
        else :
            self.__persistent = persistent

        if duration is None:
            self.__duration = 0
        else : 
            self.__duration = duration

        if expire_date is not None:
            self.__expire_date = expire_date

    @property
    def limit(self):
        return self.__limit

    @property
    def persistent(self):
        return self.__persistent

    @property
    def duration(self):
        return self.__duration

    @property
    def expire_date(self):
        return self.__expire_date

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @persistent.setter
    def persistent(self, persistent):
        self.__persistent = persistent

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @expire_date.setter
    def expire_date(self, expire_date):
        self.__expire_date = expire_date

    def playback_policy_dict(self):
        playback_policy = {"limit": self.__limit, "persistent": self.__persistent}
        if hasattr(self, "duration"):
            playback_policy["duration"] = self.__duration
        if hasattr(self, "expire_date"):
            playback_policy["expire_date"] = self.__expire_date

        return playback_policy

    # regEx - expire_date
    def _check_dates(self):
        pattern = True
        if hasattr(self, 'expire_date') :
            pattern = re.match(
                "^[0-9]{4}-[0,1][0-9]-[0-5][0-9]T([0-2][0-3]:[0-5][0-9]:[0-5][0-9])Z$",
                self.__expire_date)
        return pattern

    def _check(self):
        if (hasattr(self, "duration") or hasattr(self, "expire_date")) and self.__limit is False:
            return False