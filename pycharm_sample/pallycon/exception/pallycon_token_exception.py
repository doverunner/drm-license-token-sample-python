import json

"""
Error Code List
"""
error_list = [
    ('1000', 'Token err : The userId is Required'),
    ('1001', 'Token err : The cId is Required'),
    ('1002', 'Token err : The siteId is Required'),
    ('1003', 'Token err : The accessKey is Required'),
    ('1004', 'Token err : The siteKey is Required'),
    ('1005', 'Token err : The policy is Required'),
    ('1006', 'PlaybackPolicy : The limit should be Boolean'),
    ('1007', 'PlaybackPolicy : The persistent should be Boolean'),
    ('1008', 'PlaybackPolicy : The duration should be Integer'),
    ('1009', 'PlaybackPolicy : The expireDate time format should be \'YYYY-MM-DD\'T\'HH:mm:ss\'Z\''),
    ('1010', 'PlaybackPolicy : The limit value should be true when setting duration or expireDate'),
    ('1011', 'SecurityPolicy : The hardwareDrm must be Boolean'),
    ('1012', 'SecurityPolicy : The allowMobileAbnormalDevice should be Boolean'),
    ('1013', 'SecurityPolicy : The playreadySecurityLevel should be Integer'),
    ('1014', 'SecurityPolicy : The playreadySecurityLevel should be in 150 or more'),
    ('1015', 'SecurityPolicy : The allowExternalDisplay should be Boolean'),
    ('1016', 'SecurityPolicy : The controlHdcp should be Integer'),
    ('1017', 'HlsAes : The Key should be 16byte hex String'),
    ('1018', 'HlsAes : The Iv should be 16byte hex String'),
    ('1019', 'MpegCenc : The KeyId should be 16byte hex String'),
    ('1020', 'MpegCenc : The Key should be 16byte hex String'),
    ('1021', 'MpegCenc : The Iv should be 16byte hex String'),
    ('1022', 'Ncg : The Cek should be 32byte hex String')
]
error_dict = dict(error_list)

class PallyConTokenException(Exception):

    def __init__(self, code='0000'):
        self.__code = code
        if code is not '0000':
            self.__message = error_dict[code]
        else:
            self.__message = 'success'

    def error_message(self):
        json_str = {
            self.__code: self.__message
        }
        return json.dumps(json_str)
