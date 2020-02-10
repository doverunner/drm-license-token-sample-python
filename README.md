# Drm-token-Sample-PYTHON





<br>

## Prerequisites

### Language

This works on `PYTHON` version : 

- 3.7.6 and greater

<br>

### IDE

- PyCharm
- VS code

<br>

### Libraries

```bash
pytz==2019.3
```

see other Libraries installed in this project : `requirements.txt`





<br><br>

## Directories

| dir |                   |    description  |
| -------- | ----------------- | ---- |
|vscode_sample/pallycon|  |      |
|          | /sample/exception | exception code |
|          | /sample/token     | source directory |
|          | /test             | test (unittest) |
|pycharm_sample/pallycon|  |      |
|          | /exception | exception package |
|          | /token    | source directory |
|          | /test             | token sample @`client_test.py` |

<br>

### How to get token

0. make **quick** token : go to `pallycon/test/client_test.py`

1. Before get token, you need to set up `policy`.

   ```python
   from policy_request import PolicyRequest as Policy
   policy = Policy()
   
   (
   	policy
           .set_playback_policy(playback)
           .set_security_policy(security)
           .set_external_key(external)
   )
   ```

   

2. As you can see above, you need to decide whether to set `playback`, `security`, or `external`.

   If you want to set up all policies, 

   ```python
   from playback_policy_request import PlaybackPolicyRequest as Playback
   from security_policy_request import SecurityPolicyRequest as Security
   from external_key_request import ExternalKeyRequest as ExternalKey
   
   playback = Playback()
   security = Security()
   external = ExternalKey()
   
   
   def set_playback_policy():
       playback.limit = True
       playback.duration = 800
       playback.expire_date = '2020-11-15T11:11:30Z'
   
   def set_security_policy():
       security.hardware_drm = True
       security.output_protect = set_output_protect(
       security.playready_security_level = 1700
   
   def set_external_key():
       """
       ### set mpeg_cecn | hls_aes | ncg
       """
       external.mpeg_cenc = set_mpeg_cenc()
       external.hls_aes = set_hls_aes()
       external.ncg = set_ncg()
   
   def set_output_protect():
       from output_protect_request import OutputProtectRequest as OutputProtect
       output_protect = OutputProtect()
       output_protect.allow_external_display = True
       output_protect.control_hdcp = 2
       return output_protect    
           
   def set_mpeg_cenc():
       from mpeg_cenc_request import MpegCencRequest
       key_id = 'd5f1a1aa55546666d5f1a1aa55546666'
       key = '11b11af515c10000fff111a1aef51510'
       iv = 'f15111a331f15af515c10ef011b00fa0'
       mpeg_cenc = MpegCencRequest(key_id, key, iv)
       return mpeg_cenc
       
   def set_hls_aes():
       from hls_aes_request import HlsAesRequest
       key = '1111aaef51510000ffff1111aaef5151'
       iv = '11115555444477776666000033332222'
       hls_aes = HlsAesRequest(key,iv)
       return hls_aes
   
   def set_ncg():
       from ncg_request import NcgRequest
       cek = 'd5f1a1aa55546666d5f1a1aa55546666f15111a331f15af515c10ef011b00fa0'
       ncg = NcgRequest(cek)
       return ncg    
   ```

   

3. Import `PallyConDrmTokenClient` from `pallycon_drm_token_client.py`

   ```python
   from pallycon_drm_token_client import PallyConDrmTokenClient as TokenClient 
   def set_drm_token():
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
   ```



4. Make encrypted token !

   ```python
   def get_drm_token():
       result = token.execute()
   
   print (result)
   ```

   if there are minor mistakes when created, `result` will return error messages we already made on  `error_code.py` or you can see the messages below. Follow the comment and fix the bugs.

   







### Error Messages

| Error Code | Error Messages                                               |
| ---------- | ------------------------------------------------------------ |
| 1000       | Token err : The userId is Required                           |
| 1001       | Token err : The cId is Required                              |
| 1002       | Token err : The siteId is Required                           |
| 1003       | Token err : The accessKey is Required                        |
| 1004       | Token err : The siteKey is Required                          |
| 1005       | Token err : The policy is Required                           |
| 1006       | PlaybackPolicy : The limit should be Boolean                 |
| 1007       | PlaybackPolicy : The persistent should be Boolean            |
| 1008       | PlaybackPolicy : The duration should be Integer              |
| 1009       | PlaybackPolicy : The expireDate time format should be `YYYY-MM-DD'T'HH:mm:ss'Z` |
| 1010       | PlaybackPolicy : The limit value should be true when setting duration or expireDate |
| 1011       | SecurityPolicy : The hardwareDrm must be Boolean             |
| 1012       | SecurityPolicy : The allowMobileAbnormalDevice should be Boolean |
| 1013       | SecurityPolicy : The playreadySecurityLevel should be Integer |
| 1014       | SecurityPolicy : The playreadySecurityLevel should be in 150 or more |
| 1015       | SecurityPolicy : The allowExternalDisplay should be Boolean  |
| 1016       | SecurityPolicy : The controlHdcp should be Integer           |
| 1017       | HlsAes : The Key should be 16byte hex String                 |
| 1018       | HlsAes : The Iv should be 16byte hex String                  |
| 1019       | MpegCenc : The KeyId should be 16byte hex String             |
| 1020       | MpegCenc : The Key should be 16byte hex String               |
| 1021       | MpegCenc : The Iv should be 16byte hex String                |
| 1022       | Ncg : The Cek should be 32byte hex String                    |









