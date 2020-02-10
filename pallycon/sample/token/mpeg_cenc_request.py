class MpegCencRequest:

    """
    MpegCencRequest constructor
    @param key_id
    @param key
    @param iv 
    """
    
    def __init__(self, key_id, key, iv):
        self.__key_id = key_id
        self.__key = key
        self.__iv = iv

    @property
    def key_id(self):
        return self.__key_id

    @property
    def key(self):
        return self.__key
        
    @property
    def iv(self):
        return self.__iv

    @key_id.setter
    def key_id(self, key_id):
        self.__key_id = key_id
    
    @key.setter
    def key(self, key):
        self.__key = key

    @iv.setter
    def iv(self, iv):
        self.__iv = iv

    """
    returns dictionary type of MpegCencRequest
    """
    def mpeg_cenc_dict(self):
        mpeg_cenc = {
            'key_id': self.__key_id,
            'key': self.__key,
            'iv': self.__iv
        }
        return mpeg_cenc