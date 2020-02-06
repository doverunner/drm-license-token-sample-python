
class NcgRequest:

    """
    NcgRequest constructor
    @param cek 
    """

    def __init__(self, cek):
        self.__cek = cek

    @property
    def cek(self):  #getter
        return self.__cek

    @cek.setter
    def cek(self, cek):  #setter
        self.__cek = cek

    
    def ncg_dict(self):
        ncg = {'cek' : self.__cek}
        return ncg
