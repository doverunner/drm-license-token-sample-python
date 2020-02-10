from pallycon.token.policy.mpeg_cenc_request import MpegCencRequest
from pallycon.token.policy.hls_aes_request import HlsAesRequest
from pallycon.token.policy.ncg_request import NcgRequest

class ExternalKeyRequest:

    def __init__(self, mpeg_cenc=None, hls_aes=None, ncg=None):
        if isinstance(mpeg_cenc, MpegCencRequest):
            self.__mpeg_cenc = mpeg_cenc
        if isinstance(hls_aes, HlsAesRequest):
            self.__hls_aes = hls_aes
        if isinstance(ncg, NcgRequest):
            self.__ncg = ncg

    @property
    def mpeg_cenc(self):
        return self.__mpeg_cenc

    @property
    def hls_aes(self):
        return self.__hls_aes

    @property
    def ncg(self):
        return self.__ncg

    @mpeg_cenc.setter
    def mpeg_cenc(self, mpeg_cenc):
        self.__mpeg_cenc = mpeg_cenc

    @hls_aes.setter
    def hls_aes(self, hls_aes):
        self.__hls_aes = hls_aes

    @ncg.setter
    def ncg(self, ncg):
        self.__ncg = ncg

    def external_key_dict(self):
        external_key = {}
        if hasattr(self, 'mpeg_cenc'):
            external_key['mpeg_cenc'] = self.__mpeg_cenc.mpeg_cenc_dict()
        if hasattr(self, 'hls_aes'):
            external_key['hls_aes'] = self.__hls_aes.hls_dict()
        if hasattr(self, 'ncg'):
            external_key['ncg'] = self.__ncg.ncg_dict()
        return external_key
