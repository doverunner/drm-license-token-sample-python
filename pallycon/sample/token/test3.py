
import json
import pallycon_drm_token_client
from pallycon_drm_token_client import PallyConDrmTokenClient
import policy_request
from policy_request import PolicyRequest 
import playback_policy_request 
from playback_policy_request import PlaybackPolicyRequest as Playback
import external_key_request
from external_key_request import ExternalKeyRequest

"""
exception set
"""
import sys, os
dir_path = os.path.dirname(sys.path[0])
new_dir_path = os.path.join(dir_path, 'exception/')
sys.path.append(new_dir_path)

import pallycon_token_exception as token_exception
from pallycon_token_exception import PallyConTokenException

playback_t = Playback(True, None, None, '2020-15-15T11:11:30')
# playback_t.limit = False
# playback_t.persistent = 'Texttt'
# playback_t.duration = 300
playback_t.expire_date = '2020-11-15T11:11:30Z'

# print('playback \n\t', json.dumps(playback_t.playback_policy_dict()))

policy = PolicyRequest(playback_t)


def set_external_key():
    from mpeg_cenc_request import MpegCencRequest
    external_key = ExternalKeyRequest()

    # key_id = 'd5f1a1aa55546666d5f1a1aa55546666'
    key_id = 'TESTd5f16testttt'
    key = '11b11af515c10000fff111a1aef51510'
    iv = 'f15111a331f15af515c10ef011b00fa0'
    
    mpeg = MpegCencRequest(key_id, key, iv)

    # print('mepg test : ', json.dumps(mpeg.mpeg_cenc_dict()))
    external_key.mpeg_cenc = mpeg

    policy.set_external_key(external_key) 


client = (
    PallyConDrmTokenClient()
    .playready()
    .site_key("FDs3PWlU5WlU5D8oLl8oLlFWkCs3PWkC")
    .access_key("FDs3PLT2FVJDp4Di18z6lzv3DKvNOP20")
    .site_id("TEST-ID")
    .user_id("tester-user")
    .cid("disney-frozen")
)

set_external_key()
client.policy(policy)



"""
### set log ###
"""
import logging
logger = logging.getLogger('TEST_LOG')
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

logger.addHandler(consoleHandler)

formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
consoleHandler.setFormatter(formatter)

logger.info('information message')

logger.info('policy:\t ' + policy.toJsonString())

result=client.execute()
logger.debug(client.execute())
logger.info('result:\t '+ result)
logger.info ('user-id:\t ' + client.get_user_id())
