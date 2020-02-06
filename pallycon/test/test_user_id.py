import sys, os
from pathlib import Path

set_path = Path(os.path.abspath(__file__)).parents[1]
join_path = os.path.join(set_path, 'sample', 'token/')
sys.path.append(join_path)

"""
unit test
"""


from pallycon_drm_token_client import PallyConDrmTokenClient
import unittest
import logging

"""
logger = logging.getLogger('TEST_LOG')
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.addHandler(consoleHandler)

formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
consoleHandler.setFormatter(formatter)

logger.info('information message')
"""


# logging.basicConfig(
#     format='%(process)d-%(levelname)s-%(message)s', 
#     datefmt='%m/%d/%Y %I:%M:%S %p',
#     level=logging.DEBUG,
#     handlers=[
#         logging.FileHandler("debug.log"),
#         logging.StreamHandler
#     ]
# )
# logging.info('test ')
# logger = logging.getLogger('TEST_LOG')
# logger.setLevel(logging.DEBUG)


class Test_Practice(unittest.TestCase):
    
    def setUp(self):
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
        self.assertEqual(self.client.get_user_id(), 'tester-user')

    def test_site_key(self):
        self.assertEqual(self.client.get_site_key(), 'FDs3PWlU5WlU5D8oLl8oLlFWkCs3PWkC')

    def test_excute(self):

        result = self.client.execute()
        return result
        # logging.debug(result)


if __name__ == '__main__':
    unittest.main()


# logging.debug(Test_Token_User_ID().test_excute())