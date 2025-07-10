from doverunner.exception.doverunner_token_exception import DoveRunnerTokenException
from doverunner.token.v2.security_policy_widevine import SecurityPolicyWidevine
from doverunner.token.v2.security_policy_playready import SecurityPolicyPlayready
from doverunner.token.v2.security_policy_fairplay import SecurityPolicyFairplay
from doverunner.token.v2.security_policy_ncg import SecurityPolicyNcg
from doverunner.token.v2.security_policy_wiseplay import SecurityPolicyWiseplay


class SecurityPolicy:
    def __init__(self):
        self.__security_track_type = 'ALL'
        self.__security_widevine = None
        self.__security_playready = None
        self.__security_fairplay = None
        self.__security_ncg = None
        self.__security_wiseplay = None

    """ setter """
    def track_type(self, track_type: str):
        from doverunner.config.common.track_type import check
        if isinstance(track_type, str) and check(track_type):
            self.__security_track_type = track_type
        else:
            raise DoveRunnerTokenException('1013')
        return self

    def widevine(self, widevine: SecurityPolicyWidevine):
        if isinstance(widevine, SecurityPolicyWidevine):
            self.__security_widevine = widevine.dict()
        else:
            raise DoveRunnerTokenException('1014')
        return self

    def playready(self, playready: SecurityPolicyPlayready):
        if isinstance(playready, SecurityPolicyPlayready):
            self.__security_playready = playready.dict()
        else:
            raise DoveRunnerTokenException('1015')
        return self

    def fairplay(self, fairplay: SecurityPolicyFairplay):
        if isinstance(fairplay, SecurityPolicyFairplay):
            self.__security_fairplay = fairplay.dict()
        else:
            raise DoveRunnerTokenException('1016')
        return self

    def ncg(self, ncg: SecurityPolicyNcg):
        if isinstance(ncg, SecurityPolicyNcg):
            self.__security_ncg = ncg.dict()
        else:
            raise DoveRunnerTokenException('1062')
        return self

    def wiseplay(self, wiseplay: SecurityPolicyWiseplay):
        if isinstance(wiseplay, SecurityPolicyWiseplay):
            self.__security_wiseplay = wiseplay.dict()
        else:
            raise DoveRunnerTokenException('1057')
        return self

    """ getter """
    def get_widevine(self) -> dict:
        return self.__security_widevine

    def get_playready(self) -> dict:
        return self.__security_playready

    def get_fairplay(self) -> dict:
        return self.__security_fairplay

    def get_ncg(self) -> dict:
        return self.__security_ncg

    def get_wiseplay(self) -> dict:
        return self.__security_wiseplay

    def dict(self) -> dict:
        security_policy = {
            'track_type': self.__security_track_type
        }
        if self.__security_widevine is not None:
            security_policy['widevine'] = self.__security_widevine
        if self.__security_playready is not None:
            security_policy['playready'] = self.__security_playready
        if self.__security_fairplay is not None:
            security_policy['fairplay'] = self.__security_fairplay
        if self.__security_ncg is not None:
            security_policy['ncg'] = self.__security_ncg
        if self.__security_wiseplay is not None:
            security_policy['wiseplay'] = self.__security_wiseplay

        return security_policy