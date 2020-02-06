import sys, os
from pathlib import Path

set_path = Path(os.path.abspath(__file__)).parents[1]
join_path = os.path.join(set_path, 'sample', 'token/')
sys.path.append(join_path)

"""
unit test
"""
from pallycon_drm_token_client import PallyConDrmTokenClient as TokenClient 

from policy_request import PolicyRequest as Policy
from playback_policy_request import PlaybackPolicyRequest as Playback
from security_policy_request import SecurityPolicyRequest as Security
from external_key_request import ExternalKeyRequest as ExternalKey

from output_protect_request import OutputProtectRequest as OutputProtect
from mpeg_cenc_request import MpegCencRequest
from hls_aes_request import HlsAesRequest
from ncg_request import NcgRequest

import unittest

class Test_Token(unittest.TestCase):
    
    def setUp(self):
        # self.token = set_drm_token()
        self.__output_protect = OutputProtect(True, 2)
        self.__mpeg_cenc = MpegCencRequest(
            'd5f1a1aa55546666d5f1a1aa55546666', 
            '11b11af515c10000fff111a1aef51510', 
            'f15111a331f15af515c10ef011b00fa0'
            )
        self.__hls_aes = HlsAesRequest('1111aaef51510000ffff1111aaef5151', '11115555444477776666000033332222')
        self.__ncg = NcgRequest('d5f1a1aa55546666d5f1a1aa55546666f15111a331f15af515c10ef011b00fa0')

        self.__playback = Playback(True, None, 800, '2020-11-15T11:11:30Z')

        self.__security = Security(True, self.__output_protect, False, 1700)
        self.__external = ExternalKey(self.__mpeg_cenc, self.__hls_aes, self.__ncg)
        self.__policy = Policy(self.__playback, self.__security, self.__external)

        self.token = (
            TokenClient()
                .widevine()
                .site_key("FDs3PWlU5WlU5D8oLl8oLlFWkCs3PWkC")
                .access_key("FDs3PLT2FVJDp4Di18z6lzv3DKvNOP20")
                .site_id("TEST-ID")
                .user_id("tester-user")
                .cid("disney-frozen")
                .policy(self.__policy)
        )


    def test_drm_type(self):
        self.assertEqual(self.token.get_drm_type(), 'Widevine')


    def test_playback_duration(self):
        self.assertEqual(self.token.get_policy().playback_policy.duration , 800)

if __name__ == '__main__':
    unittest.main()
