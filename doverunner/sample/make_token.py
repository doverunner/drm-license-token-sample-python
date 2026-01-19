import logging
import json
import configparser
import os
from doverunner.token.doverunner_drm_token_client import DoverunnerDrmTokenClient as Token
from doverunner.token.doverunner_drm_token_policy import DoverunnerDrmTokenPolicy as Policy
from doverunner.token.doverunner_drm_token_policy import PlaybackPolicy
from doverunner.token.doverunner_drm_token_policy import SecurityPolicy
from doverunner.token.doverunner_drm_token_policy import ExternalKey
from doverunner.exception.doverunner_token_exception import DoverunnerTokenException

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
### load configuration ###
"""
def load_config():
    """
    Load configuration from config.ini file in project root.
    If config.ini doesn't exist, raise an error with instructions.
    """
    # Find project root (2 levels up from this file: sample -> doverunner -> root)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    config_path = os.path.join(project_root, 'config.ini')
    config_example_path = os.path.join(project_root, 'config.ini.example')

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}\n"
            f"Please create config.ini based on config.ini.example:\n"
            f"  cp {config_example_path} {config_path}\n"
            f"Then fill in your actual values."
        )

    config = configparser.ConfigParser()
    config.read(config_path)

    return {
        'site_id': config.get('drm', 'site_id'),
        'site_key': config.get('drm', 'site_key'),
        'access_key': config.get('drm', 'access_key'),
        'user_id': config.get('drm', 'user_id'),
        'content_id': config.get('drm', 'content_id')
    }

"""
### set variables ###
"""
playback = PlaybackPolicy()
security = SecurityPolicy()
external = ExternalKey()
policy = Policy()

"""
makes make token you want
after set up all variables and policy through set_policy() etc,
you can now call this function set_drm_token()

if there are some mistakes when created, 
you can get the error codes and the messages we offer through 'DoverunnerTokenException'
"""


def set_drm_token():
    from doverunner.config.common import response_format

    # Load configuration from config.ini
    config = load_config()

    set_policy()
    token = Token() \
        .widevine() \
        .site_id(config['site_id']) \
        .site_key(config['site_key']) \
        .access_key(config['access_key']) \
        .user_id(config['user_id']) \
        .cid(config['content_id']) \
        .policy(policy) \
        .response_format(response_format.ORIGINAL) \
        .key_rotation(False)

    logger.info(":::::: TOKEN ::::::\n" + token.execute())
    logger.debug(':::::: BEFORE ENCRYPT TOKEN ::::::' + token.to_json_str())


def set_policy():
    """
    set up policies
    if you want to set up
        @playback_policy: use the function set_playback_policy()
        @security_policy: use the function set_security_policy()
        @external_key:    use the function set_external_key()
    """
    set_playback_policy()
    set_security_policy()
    # set_external_key()

    policy \
        .playback(playback) \
        .security(security) \
        # .external(external)

    logger.debug('policy set:\t' + policy.to_json_str())


def set_playback_policy():
    from doverunner.config.playback import allowed_track_types

    playback \
        .allowed_track_types(allowed_track_types.SD_HD) \
        .persistent(False) \
        .renewal_duration("60") \

    logger.debug('playback set:\t' + json.dumps(playback.dict()))


def set_security_policy():
    """
    ### set Widevine | Playready | Fairplay | Ncg
        `Version 1 and 2` have only one difference in how to set.
        choose version you prefer.
    """

    # version 1.
    """
    from doverunner.config.common import track_type
    from doverunner.token.v2.security_policy_widevine import SecurityPolicyWidevine as Widevine
    from doverunner.token.v2.security_policy_playready import SecurityPolicyPlayready as Playready
    from doverunner.token.v2.security_policy_fairplay import SecurityPolicyFairplay as Fairplay
    from doverunner.token.v2.security_policy_ncg import SecurityPolicyNcg as Ncg

    security.track_type(track_type.ALL) \
        .widevine(Widevine()
                  .security_level(1)
                  .required_hdcp_version('HDCP_NONE')
                  .required_cgms_flags('CGMS_NONE')
                  .override_device_revocation(False)) \
        .playready(Playready()
                   .security_level(150)
                   .digital_video_protection_level(100)
                   .analog_video_protection_level(100)
                   .digital_audio_protection_level(100)
                   ) \
        .fairplay(Fairplay()
                  .hdcp_enforcement(-1)
                  .allow_airplay(True)
                  .allow_av_adapter(True)) \
        .ncg(Ncg()
             .allow_mobile_abnormal_device(True)
             .allow_external_display(True)
             .control_hdcp(0))
    """

    # version 2.
    from doverunner.config.playready import security_level as p_security_level, digital_video_protection, \
        analog_video_protection, digital_audio_protection
    from doverunner.token.v2.security_policy_widevine import SecurityPolicyWidevine as Widevine
    from doverunner.token.v2.security_policy_playready import SecurityPolicyPlayready as Playready
    from doverunner.token.v2.security_policy_fairplay import SecurityPolicyFairplay as Fairplay
    from doverunner.token.v2.security_policy_ncg import SecurityPolicyNcg as Ncg
    from doverunner.token.v2.security_policy_wiseplay import SecurityPolicyWiseplay as Wiseplay
    from doverunner.config.widevine import required_hdcp_version, required_cgms_flags, security_level as w_security_level
    from doverunner.config.fairplay import fairplay_hdcp_enforcement
    from doverunner.config.ncg import ncg_control_hdcp
    from doverunner.config.wiseplay import security_level, wiseplay_output_control
    from doverunner.config.common import track_type

    security.track_type(track_type.ALL) \
        .widevine(Widevine()
                  .security_level(w_security_level.SW_SECURE_CRYPTO)
                  .required_hdcp_version(required_hdcp_version.HDCP_NONE)
                  .required_cgms_flags(required_cgms_flags.CGMS_NONE)
                  .override_device_revocation(False)
                  .enable_license_cipher(False)
                  .allow_test_device(True)) \
        .playready(Playready()
                   .security_level(p_security_level.LEVEL_150)
                   .digital_video_protection_level(digital_video_protection.LEVEL_100)
                   .analog_video_protection_level(analog_video_protection.LEVEL_100)
                   .digital_audio_protection_level(digital_audio_protection.LEVEL_100)
                   .enable_license_cipher(False)) \
        .fairplay(Fairplay()
                  .hdcp_enforcement(fairplay_hdcp_enforcement.HDCP_NONE)
                  .allow_airplay(True)
                  .allow_av_adapter(True)) \
        .ncg(Ncg()
             .allow_mobile_abnormal_device(False)
             .allow_external_display(True)
             .control_hdcp(ncg_control_hdcp.HDCP_NONE)) \
        .wiseplay(Wiseplay()
                      .security_level(security_level.SW_LEVEL_1)
                      .output_control(wiseplay_output_control.HDCP_NONE))

    logger.debug('security set:\t' + json.dumps(security.dict()))


def set_external_key():
    """
    ### set mpeg_cenc | hls_aes | ncg
    """
    from doverunner.token.v2.external_key_mpeg_cenc import ExternalKeyMpegCenc as MpegCenc
    from doverunner.token.v2.external_key_hls_aes import ExternalKeyHlsAes as HlsAes
    from doverunner.token.v2.external_key_ncg import ExternalKeyNcg as Ncg
    from doverunner.config.common import track_type

    hls_aes_list = [
        HlsAes(track_type.SD,
               '<key_id>',
               '<key>',
               "<iv>"),
        HlsAes(track_type.HD,
               '<key_id>',
               '<key>',
               "<iv>"),
        HlsAes(track_type.UHD1,
               '<key_id>',
               '<key>',
               "<iv>"),
        HlsAes(track_type.UHD2,
               '<key_id>',
               '<key>',
               "<iv>"),
    ]

    external \
        .mpeg_cenc(MpegCenc(track_type.HD,
                            '<key_id>',
                            '<key>',
                            '<iv>')) \
        .mpeg_cenc(MpegCenc(track_type.UHD1,
                            '<key_id>',
                            '<key>',
                            '<iv>')) \
        .mpeg_cenc(MpegCenc(track_type.UHD2,
                            '<key_id>',
                            '<key>',
                            '<iv>')) \
        .hls_aes(hls_aes_list) \
        .ncg(Ncg(track_type.ALL_VIDEO,
                 '<cek>'))

    logger.debug('external set\t' + json.dumps(external.dict()))


try:
    set_drm_token()
except DoverunnerTokenException as p:
    print(p)
