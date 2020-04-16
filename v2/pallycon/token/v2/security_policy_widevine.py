from pallycon.exception.pallycon_token_exception import PallyConTokenException

class SecurityPolicyWidevine:
    def __init__(self):
        self.__widevine_security_level = 1
        self.__widevine_required_hdcp_version = 'HDCP_NONE'
        self.__widevine_required_cgms_flags = 'CGMS_NONE'
        self.__widevine_disable_analog_output = False
        self.__widevine_hdcp_srm_rule = 'HDCP_SRM_RULE_NONE'


    """ setter """
    def security_level(self, security_level: int):
        from pallycon.config import check
        if check(security_level):
            self.__widevine_security_level = security_level
        else:
            raise PallyConTokenException('1022')
        return self

    def required_hdcp_version(self, required_hdcp_version: str):
        from pallycon.config.widevine.required_hdcp_version import check
        if check(required_hdcp_version):
            self.__widevine_required_hdcp_version = required_hdcp_version
        else:
            raise PallyConTokenException('1023')
        return self

    def required_cgms_flags(self, required_cgms_flags: str):
        from pallycon.config.widevine.required_cgms_flags import check
        if check(required_cgms_flags):
            self.__widevine_required_cgms_flags = required_cgms_flags
        else:
            raise PallyConTokenException('1024')
        return self

    def disable_analog_output(self, disable_analog_output: bool):
        if isinstance(disable_analog_output, int):
            self.__widevine_disable_analog_output = disable_analog_output
        else:
            raise PallyConTokenException('1025')
        return self

    def hdcp_srm_rule(self, hdcp_srm_rule: str):
        from pallycon.config.widevine.hdcp_srm_rule import check
        if check(hdcp_srm_rule):
            self.__widevine_hdcp_srm_rule = hdcp_srm_rule
        else:
            raise PallyConTokenException('1026')
        return self


    """ getter """
    def get_security_level(self) -> int:
        return self.__widevine_security_level

    def get_required_hdcp_version(self) -> str:
        return self.__widevine_required_hdcp_version

    def get_required_cgms_flags(self) -> str:
        return self.__widevine_required_cgms_flags

    def get_disable_analog_output(self) -> bool:
        return self.__widevine_disable_analog_output

    def get_hdcp_srm_rule(self) -> str:
        return self.__widevine_hdcp_srm_rule

    def dict(self):
        widevine = {
            'security_level': self.__widevine_security_level,
            'required_hdcp_version': self.__widevine_required_hdcp_version,
            'required_cgms_flags': self.__widevine_required_cgms_flags,
            'disable_analog_output': self.__widevine_disable_analog_output,
            'hdcp_srm_rule': self.__widevine_hdcp_srm_rule
        }
        return widevine

