import sys, os
from pathlib import Path

set_path = Path(os.path.abspath(__file__)).parents[1]
join_path = os.path.join(set_path, 'sample', 'token/')
sys.path.append(join_path)

# print('join \t', join_path)
# print(sys.path)


# from 

"""
unit test
"""
# from playback_policy_request import PlaybackPolicyRequest as Playback
# from policy_request import PolicyRequest as Policy
from pallycon_drm_token_client import PallyConDrmTokenClient
import unittest

# print(PallyConDrmTokenClient().test())

class Test_Token(unittest.TestCase):
    
    def setUp(self):
        # self.playback = Playback(True, None, None, '2020-11-15T11:11:30Z')
        # self.policy = Policy(self.playback)
        self.client = (
            PallyConDrmTokenClient()
            .playready()
            .site_key("FDs3PWlU5WlU5D8oLl8oLlFWkCs3PWkC")
            .access_key("FDs3PLT2FVJDp4Di18z6lzv3DKvNOP20")
            .site_id("TEST-ID")
            .user_id("tester-user")
            .cid("disney-frozen")
        )

    def test_user_id(self):
        self.assertEqual(self.client.get_site_key(), 'FDs3PWlU5WlU5D8oLl8oLlFWkCs3PWkC')

if __name__ == '__main__':
    unittest.main()
    