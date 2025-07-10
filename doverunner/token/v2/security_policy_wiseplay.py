from doverunner.exception.doverunner_token_exception import DoveRunnerTokenException

class SecurityPolicyWiseplay:
    def __init__(self):
        self.__wiseplay_security_level = None
        self.__wiseplay_output_control = None

    def security_level(self, security_level: int):
        # 필요시 security_level 값 검증 로직 추가
        if isinstance(security_level, int):
            self.__wiseplay_security_level = security_level
        else:
            raise DoveRunnerTokenException('1060')
        return self

    def output_control(self, output_control: int):
        # 필요시 output_control 값 검증 로직 추가
        if isinstance(output_control, int):
            self.__wiseplay_output_control = output_control
        else:
            raise DoveRunnerTokenException('1061')
        return self

    def get_security_level(self) -> int:
        return self.__wiseplay_security_level

    def get_output_control(self) -> int:
        return self.__wiseplay_output_control

    def dict(self):
        wiseplay = {}
        if self.__wiseplay_security_level is not None:
            wiseplay['security_level'] = self.__wiseplay_security_level
        if self.__wiseplay_output_control is not None:
            wiseplay['output_control'] = self.__wiseplay_output_control
        return wiseplay