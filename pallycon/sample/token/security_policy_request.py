import json
import output_protect_request
from output_protect_request import OutputProtectRequest

class SecurityPolicyRequest:

    def __init__(self, hardware_drm=None, output_protect=None, 
                allow_mobile_abnormal_device=None, playready_security_level=None):
        if isinstance(hardware_drm, bool):
            self.__hardware_drm = hardware_drm

        if isinstance(output_protect, OutputProtectRequest):
            self.__output_protect = output_protect
        else :
            self.__output_protect = OutputProtectRequest()

        if isinstance(allow_mobile_abnormal_device, bool):
            self.__allow_mobile_abnormal_device = allow_mobile_abnormal_device

        if isinstance(playready_security_level, int):
            self.__playready_security_level = playready_security_level

        if hardware_drm is None:
            self.__hardware_drm = False
            
        if allow_mobile_abnormal_device is None:
            self.__allow_mobile_abnormal_device = False

        if playready_security_level is None:
            self.__playready_security_level = 150
        
    @property
    def hardware_drm(self):
        return self.__hardware_drm

    @property
    def output_protect(self):
        return self.__output_protect

    @property
    def allow_mobile_abnormal_device(self):
        return self.__allow_mobile_abnormal_device

    @property
    def playready_security_level(self):
        return self.__playready_security_level

    @hardware_drm.setter
    def hardware_drm(self, hardware_drm):
        self.__hardware_drm = hardware_drm

    @output_protect.setter
    def output_protect(self, output_protect):
        self.__output_protect = output_protect

    @allow_mobile_abnormal_device.setter
    def allow_mobile_abnormal_device(self, allow_mobile_abnormal_device):
        self.__allow_mobile_abnormal_device = allow_mobile_abnormal_device

    @playready_security_level.setter
    def playready_security_level(self, playready_security_level):
        self.__playready_security_level = playready_security_level


    def security_policy_dict(self):
        security_policy={
            'hardware_drm': self.__hardware_drm,
            'allow_mobile_abnormal_device': self.__allow_mobile_abnormal_device,
            'playready_security_level': self.__playready_security_level
        }

        if hasattr(self, 'output_protect'):
            security_policy['output_protect'] = self.__output_protect.output_protect_dict()

        return security_policy

# security = SecurityPolicyRequest(None, None, True, None)
# print(json.dumps(security.security_policy_dict()))

"""
output = OutputProtectRequest(None, 2)
security_2 = SecurityPolicyRequest(False, output, True, 2000)
print(json.dumps(security_2.security_policy_dict()))
"""