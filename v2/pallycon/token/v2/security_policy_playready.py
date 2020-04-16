from pallycon.exception.pallycon_token_exception import PallyConTokenException

class SecurityPolicyPlayready:
    def __init__(self):
        self.__playready_security_level = 150
        self.__playready_digital_video_protection = 100
        self.__playready_analog_video_protection = 100
        self.__playready_compressed_digital_audio_protection = 100
        self.__playready_uncompressed_digital_audio_protection = 100
        self.__playready_require_hdcp_type_1 = False


    """ setter """
    def security_level(self, security_level: int):
        from pallycon.config import check
        if check(security_level):
            self.__playready_security_level = security_level
        else:
            raise PallyConTokenException('1027')
        return self

    def digital_video_protection_level(self, digital_video_protection: int):
        from pallycon.config import check
        if check(digital_video_protection):
            self.__playready_digital_video_protection = digital_video_protection
        else:
            raise PallyConTokenException('1028')
        return self

    def analog_video_protection_level(self, analog_video_protection: int):
        from pallycon.config import check
        if check(analog_video_protection):
            self.__playready_analog_video_protection = analog_video_protection
        else:
            raise PallyConTokenException('1029')
        return self

    def compressed_digital_audio_protection_level(self, compressed_digital_audio_protection: int):
        from pallycon.config import check
        if check(compressed_digital_audio_protection):
            self.__playready_compressed_digital_audio_protection = compressed_digital_audio_protection
        else:
            raise PallyConTokenException('1030')
        return self

    def uncompressed_digital_audio_protection_level(self, uncompressed_digital_audio_protection: int):
        from pallycon.config import check
        if check(uncompressed_digital_audio_protection):
            self.__playready_uncompressed_digital_audio_protection = uncompressed_digital_audio_protection
        else:
            raise PallyConTokenException('1031')
        return self

    def require_hdcp_type_1(self, require_hdcp_type_1: bool):
        if isinstance(require_hdcp_type_1, bool):
            self.__playready_require_hdcp_type_1 = require_hdcp_type_1
        else:
            raise PallyConTokenException('1032')
        return self


    """ getter """
    def get_security_level(self) -> int:
        return self.__playready_security_level

    def get_digital_video_protection_level(self) -> int:
        return self.__playready_digital_video_protection

    def get_analog_video_protection_level(self) -> int:
        return self.__playready_analog_video_protection

    def get_compressed_digital_audio_protection_level(self) -> int:
        return self.__playready_compressed_digital_audio_protection

    def get_uncompressed_digital_audio_protection_level(self) -> int:
        return self.__playready_uncompressed_digital_audio_protection

    def get_require_hdcp_type_1(self) -> bool:
        return self.__playready_require_hdcp_type_1

    def dict(self):
        playready = {
            'security_level': self.__playready_security_level,
            'digital_video_protection_level': self.__playready_digital_video_protection,
            'analog_video_protection_level': self.__playready_analog_video_protection,
            'compressed_digital_audio_protection_level': self.__playready_compressed_digital_audio_protection,
            'uncompressed_digital_audio_protection_level': self.__playready_uncompressed_digital_audio_protection,
            'require_hdcp_type_1': self.__playready_require_hdcp_type_1
        }
        return playready
