
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



"""
###### 1. set up policy
-1 playback_policy
-2 security_policy
-3 external_key
"""
import json

from policy_request import PolicyRequest as Policy
from playback_policy_request import PlaybackPolicyRequest as Playback
from security_policy_request import SecurityPolicyRequest as Security
from external_key_request import ExternalKeyRequest as ExternalKey

playback = Playback()
security = Security()
external = ExternalKey()

policy = Policy()



def set_drm_token():
    from pallycon_drm_token_client import PallyConDrmTokenClient as TokenClient 

    """
    ### set up policy
    """
    set_policy()

    token = (
        TokenClient()
            .widevine()
            .playready()
            .site_key("FDs3PWlU5WlU5D8oLl8oLlFWkCs3PWkC")
            .access_key("FDs3PLT2FVJDp4Di18z6lzv3DKvNOP20")
            .site_id("TEST-ID")
            .user_id("tester-user")
            .cid("disney-frozen")
            .policy(policy)
    )

    result = 'failed lol'
    
    result = token.execute()
    # logger.debug('execute !!!!! \n\t' + token.execute())
    logger.info('result:\t' + result)


def set_policy():
    """
    set up policies
    """
    set_playback_policy()
    set_security_policy()
    set_external_key()
    
    # policy = Policy(playback, security, external_key=external)
    (
        policy
            .set_playback_policy(playback)
            .set_security_policy(security)
            .set_external_key(external)
    )
    logger.debug('policy set:\t' + policy.toJsonString())


def set_playback_policy():
    playback.limit = True
    playback.duration = 800
    playback.expire_date = '2020-11-15T11:11:30Z'
    logger.debug('playback set:\t' + json.dumps(playback.playback_policy_dict()))

def set_security_policy():
    security.hardware_drm = True
    security.output_protect = set_output_protect()
    security.playready_security_level = 1700
    logger.debug('security set:\t' + json.dumps(security.security_policy_dict()))

def set_external_key():
    """
    ### set mpeg_cecn | hls_aes | ncg
    """
    external.mpeg_cenc = set_mpeg_cenc()
    external.hls_aes = set_hls_aes()
    external.ncg = set_ncg()
    logger.debug('external set\t' + json.dumps(external.external_key_dict()))


####### policy에 필요한 것들
def set_output_protect():
    from output_protect_request import OutputProtectRequest as OutputProtect
    output_protect = OutputProtect()
    output_protect.allow_external_display = True
    output_protect.control_hdcp = 2
    logger.debug('output_protect:\t' + json.dumps(output_protect.output_protect_dict()))
    return output_protect

""" 
### for external_key
@param set_mpeg_cenc
@param set_hls_aes
@param set_ncg
"""
def set_mpeg_cenc():
    from mpeg_cenc_request import MpegCencRequest
    # key_id = 'TESTd5f16testttt'
    key_id = 'd5f1a1aa55546666d5f1a1aa55546666'
    key = '11b11af515c10000fff111a1aef51510'
    iv = 'f15111a331f15af515c10ef011b00fa0'
    mpeg_cenc = MpegCencRequest(key_id, key, iv)
    logger.debug('mpeg_cenc set:\t' + json.dumps(mpeg_cenc.mpeg_cenc_dict()))
    return mpeg_cenc
    
def set_hls_aes():
    from hls_aes_request import HlsAesRequest
    key = '1111aaef51510000ffff1111aaef5151'
    iv = '11115555444477776666000033332222'
    hls_aes = HlsAesRequest(key,iv)
    logger.debug('hls_aes set:\t' + json.dumps(hls_aes.hls_dict()))
    return hls_aes

def set_ncg():
    from ncg_request import NcgRequest
    cek = 'd5f1a1aa55546666d5f1a1aa55546666f15111a331f15af515c10ef011b00fa0'
    ncg = NcgRequest(cek)
    logger.debug('ncg set:\t' + json.dumps(ncg.ncg_dict()))
    return ncg



# set_policy()
set_drm_token()