import logging
import json
from pallycon.token.pallycon_drm_token_client import PallyConDrmTokenClient as TokenClient
from pallycon.token.policy.policy_request import PolicyRequest, \
    PlaybackPolicyRequest, SecurityPolicyRequest, ExternalKeyRequest


"""
### set log ###
"""
logger = logging.getLogger('TEST_LOG')
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)

logger.addHandler(consoleHandler)

formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
consoleHandler.setFormatter(formatter)

"""
### set variables ###
"""
playback = PlaybackPolicyRequest()
security = SecurityPolicyRequest()
external = ExternalKeyRequest()
policy = PolicyRequest()

def set_drm_token():
    result = 'failed lol'
    set_policy()
    token = (
        TokenClient()
        .widevine()
        .site_key("CAs30W7U5e5U5D8oLl8oLlT2Sts3PWkC")
        .access_key("FDs3TEsT2VJDp4Di18z6lzv3DKvNOP20")
        .site_id("TEST-ID")
        .user_id("tester-user")
        .cid("disney-frozen")
        .policy(policy)
    )
    result = token.execute()
    logger.info('TOKEN:\t' + result)


def set_policy():
    """
    set up policies
    """
    set_playback_policy()
    set_security_policy()
    set_external_key()
    (
        policy
            .set_playback_policy(playback)
            .set_security_policy(security)
            .set_external_key(external)
    )
    logger.debug('policy set:\t' + policy.to_json_string())

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

# insert into Policies
def set_output_protect():
    from pallycon.token.policy.output_protect_request import OutputProtectRequest as OutputProtect
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
    from pallycon.token.policy.mpeg_cenc_request import MpegCencRequest
    # key_id = 'TESTd5f16testttt'
    key_id = 'd5f1a1aa55546666d5f1a1aa55546666'
    key = '11b11af515c10000fff111a1aef51510'
    iv = 'f15111a331f15af515c10ef011b00fa0'
    mpeg_cenc = MpegCencRequest(key_id, key, iv)
    logger.debug('mpeg_cenc set:\t' + json.dumps(mpeg_cenc.mpeg_cenc_dict()))
    return mpeg_cenc

def set_hls_aes():
    from pallycon.token.policy.hls_aes_request import HlsAesRequest
    key = '1111aaef51510000ffff1111aaef5151'
    iv = '11115555444477776666000033332222'
    hls_aes = HlsAesRequest(key,iv)
    logger.debug('hls_aes set:\t' + json.dumps(hls_aes.hls_dict()))
    return hls_aes

def set_ncg():
    from pallycon.token.policy.ncg_request import NcgRequest
    cek = 'd5f1a1aa55546666d5f1a1aa55546666f15111a331f15af515c10ef011b00fa0'
    ncg = NcgRequest(cek)
    logger.debug('ncg set:\t' + json.dumps(ncg.ncg_dict()))
    return ncg

set_drm_token()
