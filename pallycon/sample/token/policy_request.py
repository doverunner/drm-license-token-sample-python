from playback_policy_request import PlaybackPolicyRequest
from security_policy_request import SecurityPolicyRequest
from external_key_request import ExternalKeyRequest
import json

class PolicyRequest:
    
    def __init__(self, playback_policy=None, security_policy=None, external_key=None) :
        if isinstance(playback_policy, PlaybackPolicyRequest):
            self.__playback_policy = playback_policy
        if isinstance(security_policy, SecurityPolicyRequest):
            self.__security_policy = security_policy
        if isinstance(external_key, ExternalKeyRequest):
            self.__external_key = external_key


    # getter
    @property
    def playback_policy(self):
        return self.__playback_policy

    @property
    def security_policy(self):
        return self.__security_policy
    
    @property
    def external_key(self):
        return self.__external_key
    

    #setter
    def set_playback_policy(self, playback_policy):
        self.__playback_policy = playback_policy
        return self
    
    def set_security_policy(self, security_policy):
        self.__security_policy = security_policy
        return self

    def set_external_key(self, external_key):
        self.__external_key = external_key
        return self

    def toJsonString(self):
        json_str = json.dumps(self.build())
        return json_str

    def build(self):
        self.__validate()
        
        policy = {}
        if hasattr(self, 'playback_policy'):
            policy['playback_policy'] = self.__playback_policy.playback_policy_dict()
        if hasattr(self, 'security_policy'):
            policy['security_policy'] = self.__security_policy.security_policy_dict()
        if hasattr(self, 'external_key'):
            policy['external_key'] = self.__external_key.external_key_dict()

        return policy

    def __validate(self):
        if not hasattr(self, '_PolicyRequest__playback_policy') :
            self.__playback_policy = PlaybackPolicyRequest(None,None,None,None)
        if not hasattr(self, '_PolicyRequest__security_policy'):
            self.__security_policy = SecurityPolicyRequest(None,None,None,None)
