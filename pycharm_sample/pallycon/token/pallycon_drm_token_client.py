import json
import base64
import hashlib

from Crypto.Cipher import AES
import pytz
import datetime
from pallycon.exception.pallycon_token_exception import PallyConTokenException

class PallyConDrmTokenClient:
    def __init__(self):
        self.__drm_type = "PlayReady"
        self.__AES_IV = "0123456789abcdef"

    def site_key(self, site_key):
        self.__site_key = site_key
        return self

    def access_key(self, access_key):
        self.__access_key = access_key
        return self

    def playready(self):
        self.__drm_type = "PlayReady"
        return self

    def widevine(self):
        self.__drm_type = "Widevine"
        return self

    def fairplay(self):
        self.__drm_type = "FairPlay"
        return self

    def site_id(self, site_id):
        self.__site_id = site_id
        return self

    def user_id(self, user_id):
        self.__user_id = user_id
        return self

    def cid(self, cid):
        self.__cid = cid
        return self

    def policy(self, policy_request):
        self.__policy = policy_request
        policy = policy_request.to_json_string()
        self.__enc_policy = (self.__make_enc_policy(policy)).decode("utf-8")
        return self

    def __timestamp(self):
        timezone = pytz.timezone("UTC")
        new_datetime = datetime.datetime.now(timezone).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.__timestamp = new_datetime
        return self

    def __hash(self):
        hash_input = (
                self.__access_key
                + self.__drm_type
                + self.__site_id
                + self.__user_id
                + self.__cid
                + self.__enc_policy
                + self.__timestamp
        )

        hash_string = base64.b64encode(
            hashlib.sha256(bytes(hash_input, "utf-8")).digest()
        )
        self.__hash = hash_string.decode("utf-8")
        return self

    def execute(self):
        result = ''
        try:
            self.__validation()
            self.__timestamp()
            self.__hash()
            payload_str = json.dumps(self.__get_payload())
            result = base64.b64encode(payload_str.encode("utf-8")).decode("utf-8")

        except PallyConTokenException as p:
            result = p.error_message()

        return result

    """
    get parameters
    """
    def __get_payload(self):
        input_str = {
            "drm_type": self.__drm_type,
            "site_id": self.__site_id,
            "user_id": self.__user_id,
            "cid": self.__cid,
            "policy": self.__enc_policy,
            "timestamp": self.__timestamp,
            "hash": self.__hash,
        }
        return input_str

    def __make_enc_policy(self, msg):
        key = bytes(self.__site_key, "utf-8")
        raw = self.__pad(msg)
        iv = self.__AES_IV.encode("utf-8")
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(cipher.encrypt(raw))

    # noinspection PyMethodMayBeStatic
    def __pad(self, str):
        BS = 16
        return (str + (BS - len(str) % BS) * chr(BS - len(str) % BS)).encode("utf-8")

    def __validation(self):
        if not hasattr(self, '_PallyConDrmTokenClient__user_id'):
            raise PallyConTokenException('1000')

        if not hasattr(self, '_PallyConDrmTokenClient__cid'):
            raise PallyConTokenException('1001')

        if not hasattr(self, '_PallyConDrmTokenClient__site_id'):
            raise PallyConTokenException('1002')

        if not hasattr(self, '_PallyConDrmTokenClient__access_key'):
            raise PallyConTokenException('1003')

        if not hasattr(self, '_PallyConDrmTokenClient__site_key'):
            raise PallyConTokenException('1004')

        if not hasattr(self, '_PallyConDrmTokenClient__policy'):
            raise PallyConTokenException('1005')

        """
        policy exception
        """
        playback = self.__policy.playback_policy
        security = self.__policy.security_policy

        if not isinstance(playback.limit, bool):
            raise PallyConTokenException('1006')

        if not isinstance(playback.persistent, bool):
            raise PallyConTokenException('1007')

        if isinstance(playback.duration, bool) or not isinstance(playback.duration, int):
            raise PallyConTokenException('1008')

        if playback._check_dates() is False:
            raise PallyConTokenException('1009')

        if playback._check() is False:
            raise PallyConTokenException('1010')

        if not isinstance(security.hardware_drm, bool):
            raise PallyConTokenException('1011')

        if not isinstance(security.allow_mobile_abnormal_device, bool):
            raise PallyConTokenException('1012')
        if isinstance(security.playready_security_level, bool) or \
                not isinstance(security.playready_security_level, int):
            raise PallyConTokenException('1013')
        if 150 > security.playready_security_level:
            raise PallyConTokenException('1014')

        if not isinstance(security.output_protect.allow_external_display, bool):
            raise PallyConTokenException('1015')
        if isinstance(security.output_protect.control_hdcp, bool) or \
                not isinstance(security.output_protect.control_hdcp, int):
            raise PallyConTokenException('1016')

        if hasattr(self.__policy, '_PolicyRequest__external_key'):
            external_key = self.__policy.external_key

            if hasattr(external_key, '_ExternalKeyRequest__hls_aes'):
                hls_aes = external_key.hls_aes
                if not self.__check_hex16(hls_aes.key):
                    raise PallyConTokenException('1017')

                if not self.__check_hex16(hls_aes.iv):
                    raise PallyConTokenException('1018')

            if hasattr(external_key, '_ExternalKeyRequest__mpeg_cenc'):
                mpeg_cenc = external_key.mpeg_cenc
                if not self.__check_hex16(mpeg_cenc.key_id):
                    raise PallyConTokenException('1019')
                if not self.__check_hex16(mpeg_cenc.key):
                    raise PallyConTokenException('1020')
                if not self.__check_hex16(mpeg_cenc.iv):
                    raise PallyConTokenException('1021')

            if hasattr(external_key, '_ExternalKeyRequest__ncg'):
                ncg = external_key.ncg
                if not self.__check_hex32(ncg.cek):
                    raise PallyConTokenException('1022')

    def get_drm_type(self):
        return self.__drm_type

    def get_site_id(self):
        return self.__site_id

    def get_user_id(self):
        return self.__user_id

    def get_cid(self):
        return self.__cid

    def get_policy(self):
        return self.__policy.to_json_string()

    def get_site_key(self):
        return self.__site_key

    def get_access_key(self):
        return self.__access_key

    def get_time_stamp(self):
        return self.__timestamp

    def get_hash(self):
        return self.__hash

    # noinspection PyMethodMayBeStatic
    def __check_hex16(self, words):
        import re
        pattern = False
        test = re.compile('^[0-9a-f]{32}$')
        pattern = test.match(words)
        return pattern

    # noinspection PyMethodMayBeStatic
    def __check_hex32(self, words):
        import re
        pattern = False
        test = re.compile('^[0-9a-f]{64}$')
        pattern = test.match(words)
        return pattern


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        from pathlib import Path
        set_path = Path(path.abspath(__file__)).parents[0]
        if set_path not in sys.path:
            sys.path.append(path.dirname(set_path))
