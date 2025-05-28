from doverunner.exception.doverunner_token_exception import DoverunnerTokenException
from doverunner.config import track_type as ncg_track_type
from doverunner.config.track_type import check


class ExternalKeyNcg:

    def __init__(self, track_type: ncg_track_type = '', cek: str = ''):
        if isinstance(track_type, str) and check(track_type):
            self.__track_type = track_type
        else:
            raise DoverunnerTokenException('1046')

        if isinstance(cek, str) and _check_hex32(cek):
            self.__cek = cek
        else:
            raise DoverunnerTokenException('1047')

    @property
    def track_type(self):
        return self.__track_type

    @property
    def cek(self):
        return self.__cek

    def dict(self):
        ncg = {
            'track_type': self.__track_type,
            'cek': self.__cek
        }
        return ncg



def _check_hex32(words) -> bool:
    import re
    test = re.compile('^[0-9a-f]{64}$')
    pattern = test.match(words)
    if pattern is None:
        pattern = False
    else:
        pattern = True
    return pattern
