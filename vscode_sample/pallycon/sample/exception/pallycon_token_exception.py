import error_code
import json

"""
# list 
print(error_code.error_code) 
"""

class PallyConTokenException(Exception):

    error_code_list = error_code.error_code
    mydict = dict(error_code_list)

    def __init__(self, code='0000'):
        self.__code = code
        if code is not '0000' :
            self.__message = self.mydict[code]
        else :
            self.__message = 'success'

    def toJsonString(self):
        jsonStr = {
            self.__code : self.__message
        }
        return json.dumps(jsonStr)
    
    @property
    def code(self):
        return self.__code

    @property
    def message(self):
        return self.__message
    
