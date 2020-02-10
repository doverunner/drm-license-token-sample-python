class HlsAesRequest:
    """
    HlsAesRequest constructor
    @param key
    @param iv
    """

    def __init__(self, key, iv):
        self.__key = key
        self.__iv = iv

    @property
    def key(self):
        return self.__key

    @property
    def iv(self):
        return self.__iv

    @key.setter
    def key(self, key):
        self.__key = key

    @iv.setter
    def iv(self, iv):
        self.__iv = iv

    def hls_dict(self):
        hls = {
            'key': self.__key,
            'iv': self.__iv
        }
        return hls

