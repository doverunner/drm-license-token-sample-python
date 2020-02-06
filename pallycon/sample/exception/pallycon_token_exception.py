import error_code
import json

"""
# list 
print(error_code.error_code) 
"""

# get one
# error_message = mydict['1021']
# print (error_message)

class PallyConTokenException(Exception):

    error_code_list = error_code.error_code
    mydict = dict(error_code_list)

    def __init__(self, code='0000'):
        self.__code = code
        if code is not '0000' :
            self.__message = self.mydict[code]
        else :
            self.__message = 'success'
        # print('exception : \n\t' , self.toJsonString())

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
    

"""
# how to call
p_exception = PallyConTokenException('1022')
print(p_exception.code)
print(p_exception.message)
print(p_exception.toJsonString())
"""

# p = PallyConTokenException()
# print(p.code)
# print(p.message)