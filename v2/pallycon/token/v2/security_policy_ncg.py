from pallycon.exception.pallycon_token_exception import PallyConTokenException

class SecurityPolicyNcg:

    def __init__(self):
        self.__ncg_allow_mobile_abnormal_device = False
        self.__ncg_allow_external_display = False
        self.__ncg_control_hdcp = 0

    """ setter """
    def allow_mobile_abnormal_device(self, allow_mobile_abnormal_device: bool):
        if isinstance(allow_mobile_abnormal_device, bool):
            self.__ncg_allow_mobile_abnormal_device = allow_mobile_abnormal_device
        else:
            raise PallyConTokenException('1036')
        return self

    def allow_external_display(self, allow_external_display: bool):
        if isinstance(allow_external_display, bool):
            self.__ncg_allow_external_display = allow_external_display
        else:
            raise PallyConTokenException('1037')
        return self

    def control_hdcp(self, control_hdcp: int):
        from pallycon.config import check
        if check(control_hdcp):
            self.__ncg_control_hdcp = control_hdcp
        else:
            raise PallyConTokenException('1038')
        return self

    """ getter """
    def get_allow_mobile_abnormal_device(self) -> bool:
        return self.__ncg_allow_mobile_abnormal_device

    def get_allow_external_display(self) -> bool:
        return self.__ncg_allow_external_display

    def get_control_hdcp(self) -> int:
        return self.__ncg_control_hdcp

    def dict(self):
        ncg = {
            'allow_mobile_abnormal_device': self.__ncg_allow_mobile_abnormal_device,
            'allow_external_display': self.__ncg_allow_external_display,
            'control_hdcp': self.__ncg_control_hdcp
        }
        return ncg


